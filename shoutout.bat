@echo off
echo Running Shoutout Program...
python -c "import win32com.client, time; l=['Rahul','Nishant','Harry']; s=win32com.client.Dispatch('SAPI.SpVoice'); [s.Speak(f'Shoutout to {name}') or print(f'Shoutout to {name}') or time.sleep(0.5) for name in l]"
echo.
echo ✅ All shoutouts done!
pause
