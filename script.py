import re
import xml.etree.ElementTree as ET



def main():
    print("Hello, World!")
    
    tree = ET.parse("logo_mhs.svg")
    root = tree.getroot()
    svg_root = {}
    svg_tags = {}
    i = 0
    
    with open("tags_output.txt", "w") as f:

        for elem in root.iter():
            i += 1
            tags = f"tag_{i}"
            if i == 1:
                svg_root = elem.attrib
                pass
            else:
                svg_tags[tags] = elem.attrib
                f.write(f"{elem.tag} {elem.attrib}\n")
            
    with open("svg_output.txt", "w") as f:
        f.write(f"{svg_tags}\n")

    filtered = {k: {"d": v["d"]} for k, v in svg_tags.items() if "d" in v}
    print(filtered)

    with open("svg_output.txt", "w") as f:
        f.write(f"{filtered}\n")
        
    # Concatenate all "d" values into one long string
    all_d_paths = "".join(v["d"] for v in filtered.values())

    # Optional: save to a file for inspection
    with open("svg_output.txt", "w") as f:
        f.write(all_d_paths)






if __name__ == "__main__":
    import sys
    sys.exit(main())
# This script prints "Hello, World!" to the console and returns 0.