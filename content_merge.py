import sys
import os

subproject_path = os.path.abspath("./scripts/content_merge")
print(subproject_path)
sys.path.append(subproject_path)

import scripts.content_merge.main as content_merge


if __name__ == "__main__":
    content_merge.main()
