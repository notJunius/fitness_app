import raylib as rl


def main():
    TITLE = "traked"
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    rl.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE.encode("utf-8"))

    rl.SetTargetFPS(60)

    current_page = "home"


    while not rl.WindowShouldClose():

        match current_page:
            case "home":
                weight_button = rl.GuiButton((SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/6 * 5, 100, 50), "Log Weight".encode("utf-8"))
                if weight_button:
                    current_page = "weight"
            case "weight":
                home_button = rl.GuiButton((SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/6 * 5, 100, 50), "Home".encode("utf-8"))
                if home_button:
                    current_page = "home"
                

        

        rl.BeginDrawing()
        rl.ClearBackground(rl.GRAY)

        match current_page:
            case "home":
                rl.DrawText("Let's lose some weight you fatass".encode("utf-8"), 400, 400, 32, rl.BLUE)
            case "weight":
                rl.DrawText("Log your weight today!".encode("utf-8"), 400, 400, 32, rl.WHITE)


        rl.EndDrawing()
    rl.CloseWindow()




if __name__ == "__main__":
    main()
