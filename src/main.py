from textnode import TextNode, TextType


def main():
    test = TextNode("This is a text node test", TextType.BOLD, "https://www.testnodetest.com")
    print(test)



if __name__ == "__main__":
    main()