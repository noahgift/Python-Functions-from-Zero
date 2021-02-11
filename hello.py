def with_input(color):
    from random import choices

    words = ["red", "yellow", "green"]
    new_color = choices(words)[0]
    print(
        f"""Yesterday, my favorite color was {color}.
        Today this is my favorite color: {new_color}
        """
    )


print(with_input("blue"))
