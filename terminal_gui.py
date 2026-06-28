#!/usr/bin/env python3
import io
import sys
import os
import platform
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from tkinter.scrolledtext import ScrolledText

if sys.platform == 'win32':
    from terminal_windows import TerminalManager
else:
    from terminal import TerminalManager


class TerminalGUI:
    def __init__(self):
        self.terminal = TerminalManager()
        self.root = tk.Tk()
        self.root.title('STerminal GUI')
        self._build_ui()
        self.refresh_saved_commands()
        self.append_output('STerminal GUI ready. Type a command and press Enter or Execute.\n')

    def _build_ui(self):
        frame = ttk.Frame(self.root, padding='10')
        frame.grid(row=0, column=0, sticky='nsew')

        self.output = ScrolledText(frame, wrap='word', state='disabled', width=100, height=25)
        self.output.grid(row=0, column=0, columnspan=4, sticky='nsew')

        self.command_var = tk.StringVar()
        self.command_entry = ttk.Entry(frame, textvariable=self.command_var, width=88)
        self.command_entry.grid(row=1, column=0, columnspan=3, sticky='ew', pady=(8, 0))
        self.command_entry.bind('<Return>', self.execute_command)
        self.command_entry.focus()

        execute_button = ttk.Button(frame, text='Execute', command=self.execute_command)
        execute_button.grid(row=1, column=3, sticky='ew', padx=(8, 0), pady=(8, 0))

        save_button = ttk.Button(frame, text='Save Cmd', command=self.save_command_dialog)
        save_button.grid(row=2, column=0, sticky='ew', pady=(8, 0))

        menu_button = ttk.Button(frame, text='Menu List', command=self.show_menu_list)
        menu_button.grid(row=2, column=1, sticky='ew', padx=(8, 0), pady=(8, 0))

        clear_button = ttk.Button(frame, text='Clear Output', command=self.clear_output)
        clear_button.grid(row=2, column=2, sticky='ew', padx=(8, 0), pady=(8, 0))

        exit_button = ttk.Button(frame, text='Exit', command=self.root.quit)
        exit_button.grid(row=2, column=3, sticky='ew', padx=(8, 0), pady=(8, 0))

        saved_label = ttk.Label(frame, text='Saved Commands:')
        saved_label.grid(row=3, column=0, columnspan=4, sticky='w', pady=(12, 0))

        self.saved_list = tk.Listbox(frame, height=8, activestyle='none')
        self.saved_list.grid(row=4, column=0, columnspan=3, sticky='nsew', pady=(4, 0))
        self.saved_list.bind('<Double-Button-1>', self.run_selected_saved_command)

        remove_button = ttk.Button(frame, text='Remove Selected', command=self.remove_selected_saved_command)
        remove_button.grid(row=4, column=3, sticky='nsew', padx=(8, 0), pady=(4, 0))

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(4, weight=0)

    def append_output(self, text: str) -> None:
        self.output.config(state='normal')
        self.output.insert('end', text)
        self.output.see('end')
        self.output.config(state='disabled')

    def clear_output(self) -> None:
        self.output.config(state='normal')
        self.output.delete('1.0', 'end')
        self.output.config(state='disabled')

    def refresh_saved_commands(self) -> None:
        self.saved_list.delete(0, 'end')
        for name, command in self.terminal.saved_commands.items():
            self.saved_list.insert('end', f'{name} -> {command}')

    def execute_command(self, event=None) -> None:
        command = self.command_var.get().strip()
        if not command:
            return

        if command.lower() == 'clear':
            self.clear_output()
            self.command_var.set('')
            return

        self.append_output(self.terminal.prompt() + command + '\n')
        self.command_var.set('')

        output = self._run_terminal_command(command)
        if output:
            self.append_output(output)

        self.refresh_saved_commands()

    def _run_terminal_command(self, command: str) -> str:
        buffer = io.StringIO()
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        try:
            sys.stdout = buffer
            sys.stderr = buffer
            self.terminal.process_command(command)
        except SystemExit:
            self.root.quit()
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
        return buffer.getvalue()

    def save_command_dialog(self) -> None:
        name = simpledialog.askstring('Save Command', 'Enter a name for the saved command:')
        if not name:
            return

        command = self.command_var.get().strip()
        if not command:
            if not self.terminal.history:
                messagebox.showwarning('Save Command', 'No command to save. Enter a command or run one first.')
                return
            command = self.terminal.history[-1]

        self.terminal.saved_commands[name] = command
        self.terminal._save_saved_commands()
        self.refresh_saved_commands()
        self.append_output(f"Saved command '{name}' -> {command}\n")

    def show_menu_list(self) -> None:
        if not self.terminal.saved_commands:
            messagebox.showinfo('Saved Commands', 'No saved commands yet.')
            return

        commands = '\n'.join(f'{i+1}. {name} -> {cmd}' for i, (name, cmd) in enumerate(self.terminal.saved_commands.items()))
        messagebox.showinfo('Saved Commands', commands)

    def run_selected_saved_command(self, event=None) -> None:
        selection = self.saved_list.curselection()
        if not selection:
            return
        index = selection[0]
        name = list(self.terminal.saved_commands.keys())[index]
        self._run_saved_command(name)

    def remove_selected_saved_command(self) -> None:
        selection = self.saved_list.curselection()
        if not selection:
            return
        index = selection[0]
        name = list(self.terminal.saved_commands.keys())[index]
        del self.terminal.saved_commands[name]
        self.terminal._save_saved_commands()
        self.refresh_saved_commands()
        self.append_output(f"Removed saved command '{name}'\n")

    def _run_saved_command(self, name: str) -> None:
        result = self.terminal._resolve_saved_command(name)
        if not result:
            messagebox.showerror('Run Saved Command', f"Saved command '{name}' not found.")
            return
        _, command = result
        self.command_var.set(command)
        self.execute_command()

    def run(self) -> None:
        self.root.mainloop()


def main():
    gui = TerminalGUI()
    gui.run()


if __name__ == '__main__':
    main()
