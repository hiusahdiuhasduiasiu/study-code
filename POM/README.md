POM = Page Object Model
1.我把项目分成三层：
    底层 - BasePage（操作层）：封装了Selenium的原生方法，如get_url、quit_browser、find_elements、click、send_keys等
    中层 - LoginPage（业务层）：它继承了BasePage，它只做两件事，定义维护页面的元素的定位符和封装业务方法，如登录按钮do_login、quit——login、用户名输入框、密码输入框等，以及登录方法
    上层 - test_hy（用例层）：它只负责调用业务方法和进行断言 assert
2.驱动共享（conftest.py）：
    我利用了Pytset的conftest机制。通过scope="session"的fixture，我实现了单次初始化、全局共享的驱动管理。相比较传统的每个测试用例的诶个测试用例都开关一次浏览器，它极大的提升了测试执行效率，缩减了反馈周期。整个测试任务只启动一次浏览器。通过yield关键字，确保了测试完成后浏览器可以自动关闭，避免占用内存。
3.显示等待：
    我在BasePage中还结合了WebDriverWait，实现了元素的显式等待。比如在click之前，我会先判断元素是否可见。这样能有效解决由于网络波动导致的元素元素找不到的问题，让脚本更健壮。


