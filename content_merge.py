import sys
import os

subproject_path = os.path.abspath("./scripts/content_merge")
print(subproject_path)
sys.path.append(subproject_path)

# 如果 clone 没有将子模块 拉下来 可以使用 git submodule update --init --recursive
# 后续如果要更新子模块（拉取） git submodule update --remote --recursive
import scripts.content_merge.main as content_merge


if __name__ == "__main__":
    content_merge.main()
