<div align="center">
<img src="https://t.me/i/userpic/320/kmuav2bot.jpg" alt="kmua" width="240">

# kmua bot

干啥啥不行，喵喵第一名
</div>

分支名中的 v2 仅代表设计理念上的第二代, 不作 major version 语义.

本项目随时可能会出现 breaking change, 更新前请查阅 commit history 并做好备份.

## 自用版修改

 因为这些小修改和原项目的理念存在有一些冲突，所以不打算合并到上游。
 主要修改点：

- 头衔修改功能`/t`:增加关键词黑名单`forbidden_titles.txt`，以防群友改出类似“群主”，“真管理员”，“XX的爹”之类的头衔（群管理不受限制）
  「docker部署的需要将`/kmua/forbidden_titles.txt`映射到本机磁盘」
- 头衔修改功能`/t`:群友只能改自己的头衔，群管理可以改群里（除管理外的）任何人的头衔
- 头衔删除功能`/td`：群管理可以删任何人的，群友只能删自己的
- 以上“群管理”，不包括匿名管理

## [文档](https://kmua.unv.app)

demo: [@kmuav2bot](https://t.me/kmuav2bot)

## Contributors

<!-- readme: contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/krau">
                    <img src="https://avatars.githubusercontent.com/u/71133316?v=4" width="100;" alt="krau"/>
                    <br />
                    <sub><b>Krau</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/mokurin000">
                    <img src="https://avatars.githubusercontent.com/u/34085039?v=4" width="100;" alt="mokurin000"/>
                    <br />
                    <sub><b>莯凛</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/tjsky">
                    <img src="https://avatars.githubusercontent.com/u/7272911?v=4" width="100;" alt="tjsky"/>
                    <br />
                    <sub><b>去年夏天</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/NyanWhite">
                    <img src="https://avatars.githubusercontent.com/u/51278093?v=4" width="100;" alt="NyanWhite"/>
                    <br />
                    <sub><b>喵白</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/ames0k0">
                    <img src="https://avatars.githubusercontent.com/u/26835631?v=4" width="100;" alt="ames0k0"/>
                    <br />
                    <sub><b>YóUnǎi</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/ImgBotApp">
                    <img src="https://avatars.githubusercontent.com/u/31427850?v=4" width="100;" alt="ImgBotApp"/>
                    <br />
                    <sub><b>Imgbot</b></sub>
                </a>
            </td>
		</tr>
		<tr>
            <td align="center">
                <a href="https://github.com/real-LiHua">
                    <img src="https://avatars.githubusercontent.com/u/65490624?v=4" width="100;" alt="real-LiHua"/>
                    <br />
                    <sub><b>Li Hua</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/Mufanc">
                    <img src="https://avatars.githubusercontent.com/u/47652878?v=4" width="100;" alt="Mufanc"/>
                    <br />
                    <sub><b>Mufanc</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/ricky8955555">
                    <img src="https://avatars.githubusercontent.com/u/24487646?v=4" width="100;" alt="ricky8955555"/>
                    <br />
                    <sub><b>Phrinky</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/leafmoes">
                    <img src="https://avatars.githubusercontent.com/u/44945631?v=4" width="100;" alt="leafmoes"/>
                    <br />
                    <sub><b>leafmoes</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/AHCorn">
                    <img src="https://avatars.githubusercontent.com/u/42889600?v=4" width="100;" alt="AHCorn"/>
                    <br />
                    <sub><b>安和</b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: contributors -end -->
