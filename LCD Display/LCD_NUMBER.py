def draw(b, n):
    format_str = "|".join(str(n))
    buffer = []
    line = []
    line_count = 2 + (b * 2)
    dash = " {} ".format("-" * b)
    blank = " {} ".format(" " * b)
    bar_left = "|{} ".format(" " * b)
    bar_right = " {}|".format(" " * b)
    bar_all = "|{}|".format(" " * b)
    dash_lines = {
        0: "23567890",
        line_count // 2: "2345689",
        line_count: "2356890"
    }
 
    for i in range(line_count + 1):
        line.clear()
        for character in format_str:
            if character == "|":
                line.append(" ")
                continue
 
            if i in dash_lines:
                if character in dash_lines[i]:
                    line.append(dash)
                else:
                    line.append(blank)
                continue
 
            if i < line_count // 2:
                if character in "4890":
                    line.append(bar_all)
                elif character in "1237":
                    line.append(bar_right)
                else:
                    line.append(bar_left)
            else:
                if character in "086":
                    line.append(bar_all)
                elif character in "1345679":
                    line.append(bar_right)
                else:
                    line.append(bar_left)
 
        buffer.append("".join(line))
 
    return "\n".join(buffer)

N,M = map(int,input().split())

print(draw(N,M))
