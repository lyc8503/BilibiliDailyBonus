# Bilibili 活动打卡自动化

### 这个程序有什么用?

可以帮助你自动获取 B 站 \"手书嘉年华\" 和 \"夏日音乐季\" 两个活动每日奖励: 14 个硬币及投 10 个币获得的 50 经验值.

活动到 2020.09.01 结束, 要参加请尽快. :) 

### 如何使用?

#### 方法一 使用 Github Actions(最简单, 推荐)

[可以参照这里的详细说明.](https://lyc8503.gitee.io/giteepages/github-actions/)(需要同时用到本网页和说明, 建议右键链接-在新标签页中打开.)

现在也更新了 B 站[视频教程](https://www.bilibili.com/video/BV1N54y1U7BL/).

**本项目需要设置的 Secrets:**

| 名称     | 内容          |
| -------- | ------------- |
| ACCOUNT  | 你的B站用户名 |
| PASSWORD | 你的B站密码   |



#### 方法二 使用 Docker 容器(相对方法一较复杂)

1. 找一台安装好 Docker 的服务器
2. 在任意目录下执行 `git clone https://github.com/lyc8503/BilibiliDailyBonus && cd BilibiliDailyBonus`
3. 执行 `docker build -t bilibili .`
4. 安装 Cron, 并使用 cron 每天执行 `docker run --rm --env account=你的用户名 --env password=你的密码 bilibili` 

#### 方法三 直接运行 Python(不推荐)

1. 找任意一台安装好 Python 3.6 或以上版本的服务器
2. 在任意目录下执行 `git clone https://github.com/lyc8503/BilibiliDailyBonus && cd BilibiliDailyBonus`
3. 使用 pip 安装依赖库, 参考命令`pip3 install requests rsa chardet`
4. 使用 Cron 每日执行 `python3 daily_bonus.py`

