from selene import browser as android_app, be


class MobileMethods:
    @property
    def window_size(self):
        width = android_app.driver.get_window_size()['width']
        height = android_app.driver.get_window_size()['height']
        return width, height

    def swipe_up(self, max_swipes: int = 1, duration: int = 500):
        for _ in range(max_swipes):
            width, height = self.window_size
            start_x = int(width * 0.5)
            start_y = int(height * 0.85)
            end_x = int(width * 0.5)
            end_y = int(height * 0.15)
            android_app.driver.swipe(start_x, start_y, end_x, end_y, duration)
            return self

    def swipe_down(self, max_swipes: int = 1, duration: int = 500):
        for _ in range(max_swipes):
            width, height = self.window_size
            start_x = int(width * 0.5)
            start_y = int(height * 0.15)
            end_x = int(width * 0.5)
            end_y = int(height * 0.85)
            android_app.driver.swipe_up(start_x, start_y, end_x, end_y, duration)
            return self

    def find_text_with_scrolling(self, text: str, max_swipes: int = 5) -> None:
        for attempt in range(max_swipes):
            try:
                element = android_app.element(
                    ('-android uiautomator', f'new UiSelector().text("{text}")')).with_(timeout = 3)
                element.should(be.visible)
                return
            except Exception as e:
                if attempt == max_swipes - 1:
                    raise AssertionError(f"Текст '{text}' не найден после {max_swipes} попыток скроллинга") from e
                self.swipe_up()
