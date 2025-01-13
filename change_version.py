"""
 Description: 修改微信内存版本, 原理参考: https://blog.csdn.net/Scoful/article/details/139330910
"""

import os
import platform

import pymem

# Offset addresses for version 3.6.0.18
OFFSET_ADDRS = [0x22300E0, 0x223D90C, 0x223D9E8, 0x2253E4C, 0x2255AA4, 0x22585D4]
WECHATVERSION = "3.6.0.18"


def modify_wechat_version(new_version: str) -> None:
    """
    修改微信内存的版本数值, WECHATVERSION -> new_version

    Parameters
    ----------
    new_version: str
        Target WeChat version
    """
    try:
        pm = pymem.Pymem("WeChat.exe")
    except Exception as e:
        print(f"{e}, 请确认微信已打开")
        return

    WeChatWinDll = pymem.process.module_from_name(
        pm.process_handle, "WeChatWin.dll"
    ).lpBaseOfDll
    original_version_hex = version_to_hex(WECHATVERSION)
    new_version_hex = version_to_hex(new_version)

    for offset in OFFSET_ADDRS:
        addr = WeChatWinDll + offset
        addr_value = pm.read_uint(addr)
        if addr_value == original_version_hex:
            # Write the new version hex to the memory
            pm.write_uint(addr, new_version_hex)

    print("微信版本修改成功")


def version_to_hex(version: str) -> int:
    """
    微信版本号转换为16进制数

    Parameters
    ----------
    version: str
        WeChat version for convertion

    Returns
    -------
        Hax version
    """
    result = "0x6"
    version_list = version.split(".")

    for i in range(len(version_list)):
        if i == 0:
            result += f"{int(version_list[i]):x}"
            continue
        result += f"{int(version_list[i]):02x}"

    return int(result, 16)


if __name__ == "__main__":

    if platform.system() == "Windows":
        modify_wechat_version("3.9.12.15")

        print("\n")
        os.system("pause")
    else:
        print("This script only support Windows operating system...")
