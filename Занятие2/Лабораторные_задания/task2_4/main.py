if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    kolvo_probelov = 5
    nadp = ["H", "e", 'l', "l", "o"]
    for index, value in enumerate(nadp):
        kolvo_probelov += 1
        print( " "*kolvo_probelov, value)


