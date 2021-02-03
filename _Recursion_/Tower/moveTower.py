def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height - 1, withPole, fromPole, toPole)


def moveDisk(disk, frompole, topole):
    print(f"Moving disk[{disk} from {frompole} to {topole}]")


moveTower(3, "#1", "#2", "#3")
