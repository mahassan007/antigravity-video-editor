# Dependency setup

Use this procedure for an explicit skill install or setup request, and to recover missing dependencies before an edit. Run the checks and installations in the terminal. Reuse working compatible versions. Install current stable releases for missing components, selecting versions and builds compatible with the operating system, architecture, and Whisper dependencies.

## Windows

1. Check real executables using `Get-Command` and version commands. A WindowsApps store alias alone is insufficient proof of Python. Try the Python launcher and installed Python paths if the shell alias fails. Detect WinGet and the system architecture.
2. If Python is missing or incompatible, use the newest stable Python minor for which the current Whisper release and dependencies, including PyTorch, have compatible Windows builds for this system. Check official package and wheel availability before selecting the minor. If compatibility is uncertain or installation fails, try the next supported minor. With WinGet, install the matching exact `Python.Python.<major>.<minor>` package after confirming its ID, or use the official Python installer. Verify the real interpreter with its version command. Use the verified interpreter path if the shell still resolves to the store alias.
3. If FFmpeg or FFprobe is missing or the build lacks required features, use WinGet with the exact `Gyan.FFmpeg` package ID if it supports this machine. Otherwise use a compatible Windows build linked from ffmpeg.org. FFprobe ships with FFmpeg. Refresh PATH in the current shell or use the resolved executable directory. Check both version commands and verify the FFmpeg build lists the `libx264` encoder and `subtitles` and `scdet` filters.
4. Create or reuse the workspace's ignored `.venv` with the verified compatible Python. Use `& .\.venv\Scripts\python.exe -m pip install openai-whisper` if its Whisper import or CLI is missing. Use the venv interpreter explicitly, so shell activation and global pip are unnecessary. Verify the installed version and confirm `& .\.venv\Scripts\whisper.exe --help` works. Report the executable paths for future edits. Use the CPU for transcription when a usable GPU runtime is unavailable. Whisper can download the selected model on the first transcription.
5. If a shell still has an old PATH, reload its Machine and User PATH values or locate the installed binaries and invoke them by absolute path. If an installer needs user interaction, complete the other available steps and report exactly which action remains. Retry failed checks after addressing their cause.

## Other operating systems

Detect the OS and architecture. Use its supported package manager or official distribution for compatible Python and FFmpeg with FFprobe. Use a workspace-local `.venv` and its `bin/python` and `bin/whisper` executables. Apply the same version and FFmpeg capability checks.

## Report after setup

List the verified versions and executable locations, the full paths for all four workspace folders and both editing documents, and any remaining blocker. A setup-only request ends after verification and reporting. If an edit was requested, continue with the edit once its dependencies are ready.
