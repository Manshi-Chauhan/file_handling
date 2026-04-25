def find_and_replace(filename, old_word, new_word):
    try:
        # Step 1: Read file
        with open(filename, 'r') as file:
            content = file.read()

        # Check if word exists
        if old_word not in content:
            print(f"⚠️ '{old_word}' word file me nahi mila.")
            return

        # Step 2: Replace word
        updated_content = content.replace(old_word, new_word)

        # Step 3: Write back to file
        with open(filename, 'w') as file:
            file.write(updated_content)

        print("✅ Word successfully replaced and file updated!")

    except FileNotFoundError:
        print("❌ Error: File exist nahi karti.")
    except PermissionError:
        print("❌ Error: File access permission denied.")
    except Exception as e:
        print("❌ Unexpected Error:", e)


# 🔹 User Input
filename = input("Enter file name: ")
old_word = input("Enter word to find: ")
new_word = input("Enter word to replace with: ")

find_and_replace(filename, old_word, new_word)