from pathlib import Path

from log_analyzer.parser import parse_log_line, read_logs
from log_analyzer.report import build_report, count_levels


def main():
    p = Path("data/app.log")

    lines = read_logs(p)
    parsed_logs = []

    for line in lines:
        parsed_line = parse_log_line(line)

        if parsed_line is not None:
            parsed_logs.append(parsed_line)

    stats=count_levels(parsed_logs)

    result=build_report(stats)

    print(result)


if __name__=="__main__":
    main()
