import hashlib, os, datetime

BLACKLIST_HASHES = {
    "9c91a1b8c4da2d7588f3aecd76cdee7dba24d95f0874f79fa711c0b0a490e273",
    "cce955a091518aefb9693ba4e103cdc31afc138c9eb9503984bf08f5f70eff46",
    "a016313bc090d337a66dcefc7cc18a889f5c1cfc721185fa9ad7038159efb728",
    "c6ec11a31d4c28480f4ee3cc744792e12d7919cfffff5b7ca86649c904b7abda",
    "170477195896fb9c6688d56d6d6a4c3d2021fbc7cf01b38d45eb86fe94016333",
    "dbd741a45d840d06d708339f9e9824f2a0d745ea6537ca44bff233ba7441bfda",
    "049f48024f31d86c5d8bf56c3da1d7be539c877ad189fb0c5aa9a228601d19eb",
    "90efa2e75e2102942fba13cb4a5744530cd85e84fcfc8d7ddccdc17081ac3f69",
    "3e17df6d4f4f9f321f783a50e1f8b364203f181274ff217b0c2a216dff63d41f",
    "98942a0affa9721c90b097c2c6a9cd02959185526c3b7a44377a25b252a16fff",
    "c6ec11a31d4c28480f4ee3cc744792e12d7919cfffff5b7ca86649c904b7abda"
}

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def scan_directory(directory):
    scan_results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = calculate_sha256(file_path)
                if file_hash in BLACKLIST_HASHES:
                    scan_results.append(f"Malicious file detected: {file} ({file_hash})")
                else:
                    scan_results.append(f"File is safe: {file} ({file_hash})")
            except Exception as e:
                scan_results.append(f"Error scanning file {file}: {str(e)}")

    return {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scanned_directory": directory,
        "report": scan_results
    }