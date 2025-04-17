import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        duration TEXT NOT NULL       
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, duration):
    cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))
    conn.commit()

def update_video(video_id, new_name, new_duration):
    cursor.execute("UPDATE videos SET name=?, duration=? WHERE id=?", (new_name, new_duration, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager App with db ")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1': 
                list_all_videos()
            case '2': 
                name = input("Enter the video name: ")
                duration = input("Enter the video duration: ")
                add_video(name, duration)
            case '3': 
                video_id = input("Enter the video id to update: ")
                name = input("Enter the video name: ")
                duration = input("Enter the video duration: ")
                update_video(video_id, name, duration)
            case '4': 
                video_id = input("Enter the video id to delete: ")
                delete_video(video_id)
            case '5': 
                break
            case _:
                print("Invalid choice!")

    conn.close()

if __name__ == "__main__":
    main()