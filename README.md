# Antigravity Video Editor

My content studio

A workspace skill for editing short talking-head videos from your own footage, a reference, and reusable B-roll.

## Open in Antigravity

Clone this repository, then open the cloned folder as an Antigravity workspace. If using a ZIP, extract it and open the inner `antigravity-video-editor` folder. The entry point is `.agents/skills/video-editor/SKILL.md`.

Paste this into Antigravity:

> Read README.md and use the video-editor workspace skill. Check Git, Python, FFmpeg and FFprobe as applicable, and check for a local Whisper CLI. Tell me exactly where to put my raw recording, reference video and B-roll. Show me where to customize the editing rulebook and brand sheet.

Install Python 3 and an FFmpeg build with FFprobe, H.264 encoding and the subtitles filter. For local transcription, install OpenAI Whisper in your Python environment with `python -m pip install openai-whisper`, or supply an SRT you already have. Use a vision-capable Antigravity session that can inspect extracted screenshots. If image inspection is unavailable, provide timestamped style notes or attach screenshots to the agent chat.

## Four folders

| Folder | Contents |
| --- | --- |
| `.agents/` | Skill, rulebook, brand sheet and reference-frame script |
| `inspiration/` | One subfolder per video. Add `raw.mp4`, `reference.mp4` and optional `brief.md` or `raw.srt`. |
| `b-roll/` | Reusable clips. Describe what is visible in each filename. |
| `outputs/` | Edit plan, captions and rendered MP4, organized by job and revision. |

Example job folder: `inspiration/broken-links/`. Copy `inspiration/BRIEF.template.md` to `inspiration/broken-links/brief.md` if you want to specify what to borrow from the reference. Once media is ready, ask:

> Use the video-editor skill to edit inspiration/broken-links and render the MP4.

Media and renders in these folders are ignored by Git by default. The rules and colors are editable starter defaults.
