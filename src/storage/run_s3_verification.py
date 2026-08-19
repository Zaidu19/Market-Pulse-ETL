from src.storage.s3_verification import list_raw_objects


def main() -> None:
    objects = list_raw_objects()

    print(f"Objects found: {len(objects)}")

    for object_key in objects:
        print(object_key)


if __name__ == "__main__":
    main()