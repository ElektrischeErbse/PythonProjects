import csv

def read_csv(csv_file: str):
    with open(csv_file, "r", newline='', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        items = [item for item in reader]
        _ = items.pop(0)
        return items


def make_msgs(items: list[list[str]])->dict[str,str]:
    msgs: dict[str,str] = {}
    for item in items:
        name = item[0]
        message = item[1]
        address = item[2]
        msg = f"{name}-同学, 消息: {message}, 地址: {address}"
        msgs[name] = msg
    return msgs


def send_msg(name: str, msg: str) -> bool:
    # TODO: Implement send msg function
    _ = name
    _ = msg
    return True

if __name__ == "__main__":
    items = read_csv("messages.csv")
    msgs = make_msgs(items)
    # print(msgs)
    for name in msgs.keys():
        if send_msg(name, msgs[name]):
            print(f"Send msg: {msgs[name]} to {name} success")
