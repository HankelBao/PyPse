class CodeLine():
    def __init__(self, file_name: str, line_num: int, content: str):
        self.file_name = file_name
        self.line_num = line_num
        self.content = content

    def getWordByIndex(index: int) -> str:
        return self.content[index]


def precompile_file(f) -> list:
    file_name = f.name
    code_lines = []
    line_num = 0
    with open(file_name, "r") as f:
        for line_str in f:
            line_num += 1
            line_str = line_str.strip("\n").strip()
            code_line = CodeLine(file_name, line_num, line_str)
            code_lines.append(code_line)
    return code_lines
