from PySquashfsImage import SquashFsImage

image = SquashFsImage.from_file('./openwrt-11.19.2023-x86-64-generic-squashfs-combined.img')
for item in image:
    print(item.name)
image.close()