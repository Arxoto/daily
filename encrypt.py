import argparse
import logging
import os

from Crypto.Cipher import AES

logger = logging.getLogger()


class Context(object):
    def __init__(self, encrypt: bool) -> None:
        self.cwd = "."  # os.getcwd()
        self.encrypt = encrypt
        self.source_folder = "origin" if encrypt else "encrypted"
        self.target_folder = "encrypted" if encrypt else "decrypted"
        self.encrypt_key = b"0Ooq0QoCDoO0Oo0q"

    def load_encrypt_key(self):
        with open("encrypt_key", "r", encoding="utf-8") as f:
            self.encrypt_key = f.read().encode("utf-8")
        if len(self.encrypt_key) != 16:
            raise Exception("len of encrypt_key must be 16")


CTX = Context(True)


def source_files():
    folder_path = os.path.join(CTX.cwd, CTX.source_folder)
    for file in os.listdir(folder_path):
        yield (file, os.path.join(folder_path, file))


def target_path(source_file_name: str):
    return os.path.join(CTX.cwd, CTX.target_folder, source_file_name)


def encrypt(ss: bytes, key: bytes):
    ln = AES.block_size - len(ss) % AES.block_size
    if ln == 0:
        ss = ss + AES.block_size * b"\0"
    else:
        ss = ss + ln * b"\0"  # 补全长度 16 的倍数

    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(ss)


def decrypt(bb: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_ECB)
    msg = cipher.decrypt(bb)
    return msg.rstrip(b"\0")


def do_action(source: str, target: str):
    logger.info(">>>>>>>>> %s", source)
    try:
        if CTX.encrypt:
            with open(source, "rb") as sf:
                bts = encrypt(sf.read(), CTX.encrypt_key)
                with open(target, "wb") as tf:
                    tf.write(bts)
        else:
            with open(source, "rb") as sf:
                bts = decrypt(sf.read(), CTX.encrypt_key)
                with open(target, "wb") as tf:
                    tf.write(bts)
    except Exception as e:
        logger.exception("action exception: %s", e)
    logger.info("<<<<<<<<< %s", target)


def do_loop():
    for file_info in source_files():
        do_action(file_info[1], target_path(file_info[0]))


def init(encrypt: bool):
    if encrypt:
        return
    global CTX
    CTX = Context(False)


def main():
    logging.basicConfig(
        format="%(asctime)s [%(name)s::%(levelname)s] %(message)s",
        level=logging.INFO,
    )

    # parse the args
    parser = argparse.ArgumentParser(description="encrypt or decrypt files")
    parser.add_argument(
        "-d",
        action="store_true",
        help="use decrypt action (default action is encrypt)",
    )
    args = parser.parse_args()
    init(not args.d)

    # the default
    # init(True)
    # init(False)
    CTX.load_encrypt_key()
    do_loop()


if __name__ == "__main__":
    main()
    logger.info("========= end")
