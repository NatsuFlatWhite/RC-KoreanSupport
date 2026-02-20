import os, sys, shutil

PATH = "Raycity.exe"
BACKUP = PATH + ".bak"

PATCH = [(0xC433C, 0x6E, 0x16),]

if not os.path.exists(PATH):
    sys.exit(f"대상 파일을 찾을 수 없습니다: {PATH}")

if not os.path.exists(BACKUP):
    shutil.copy2(PATH, BACKUP)
    print(f"백업 생성: {BACKUP}")
else:
    print(f"백업이 이미 존재함: {BACKUP}")

with open(PATH, "rb") as f:
    data = bytearray(f.read())

for off, orig, val in PATCH:
    before = data[off]

    if before != orig:
        sys.exit(
            f"패치 중단: 0x{off:X} 값이 예상과 다름" #SEA 590만 쓰삼
            f"(현재=0x{before:02X}, 예상=0x{orig:02X})"
        )

    data[off] = val
    print(f"0x{off:X}: 0x{before:02X} → 0x{val:02X}")

with open(PATH, "wb") as f:
    f.write(data)