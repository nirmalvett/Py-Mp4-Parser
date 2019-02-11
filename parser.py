from mp4 import MP4


def parse(file_path: str):
    with open(file_path, 'rb') as file:
        return MP4(file)


if __name__ == '__main__':
    mp4 = parse('test.mp4')
    print(mp4)
