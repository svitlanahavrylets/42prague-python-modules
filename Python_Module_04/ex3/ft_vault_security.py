def secure_archive(
        filename: str, action: str = "read", content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r", encoding="utf-8") as f:
                file_data = f.read()
            return (True, file_data)
        elif action == "write":
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, f"Unknown action: {action}")
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    res1 = secure_archive("/not/existing/file", "read")
    print(f"{res1}")
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    res2 = secure_archive("/etc/shadow", "read")
    print(f"{res2}")
    print()
    print("Using 'secure_archive' to read from a regular file:")
    res3 = secure_archive("ancient_fragment.txt", "read")
    print(f"{res3}")
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    res4 = secure_archive("new_ancient_fragment.txt", "write", "new content")
    print(f"{res4}")
