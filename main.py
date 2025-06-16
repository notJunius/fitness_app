import raylib as rl


def main():
    TITLE = "traked"
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    rl.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE.encode("utf-8"))

    rl.SetTargetFPS(60)

    while not rl.WindowShouldClose():
        

        rl.BeginDrawing()

        rl.ClearBackground(rl.GRAY)
        rl.EndDrawing()
    rl.CloseWindow()




if __name__ == "__main__":
    main()
