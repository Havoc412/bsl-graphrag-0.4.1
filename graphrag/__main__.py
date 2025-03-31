# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""The GraphRAG package."""

from .cli.main import app

app(prog_name="graphrag")


# DEBUG local
# import os
# import sys

# if __name__ == "__main__":
#     print("当前工作路径:", os.getcwd())
#     from cli.main import _query_cli

#     _query_cli(
#         method='local',
#         query='COX 是什么？',
#         root='./ragtest-cn'
#     )
