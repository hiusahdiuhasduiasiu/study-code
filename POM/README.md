POM = Page Object Model
面试描述： “我为商城项目搭建了基于 POM 的自动化框架，实现了业务逻辑与测试脚本的分离。”
1.我把项目分成三层：
    底层 - BasePage（操作层-基层）：封装了Selenium的原生方法，如get_url、quit_browser、find_elements、click、send_keys等
    中层 - LoginPage（业务层）：它继承了BasePage，它只做两件事，定义维护页面的元素的定位符和封装业务方法，如登录do_login、推出quit_login、搜索输入框search_input等，以及登录方法
    上层 - test_hy（用例层）：它只负责调用业务方法和进行断言 assert
2.驱动共享（conftest.py）：
    我利用了Pytset的conftest机制。通过scope="session"的fixture，我实现了单次初始化、全局共享的驱动管理。相比较传统的每个测试用例的诶个测试用例都开关一次浏览器，它极大的提升了测试执行效率，缩减了反馈周期。整个测试任务只启动一次浏览器。通过yield关键字，确保了测试完成后浏览器可以自动关闭，避免占用内存。
3.显示等待：
    我在BasePage中还结合了WebDriverWait，实现了元素的显式等待。比如在click之前，我会先判断元素是否可见。这样能有效解决由于网络波动导致的元素元素找不到的问题，让脚本更健壮。

conftest.py -- 管理浏览器驱动
    第一步：把driver放在conftest.py里面，全局生效
    第二部：使用@pytest.fixture(scope="session")，保证只启动一次
    第三部：使用yield确保测试结束自动关闭浏览器
    第四部：预留了分布式接口，方便后续集成到Jenkins节点


