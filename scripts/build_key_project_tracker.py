from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.table import Table, TableStyleInfo

OUT = Path(r"outputs/智言_重点项目试点与证据记录表.xlsx")

# ── 配色（一次性集中定义，改主题只动这里）──
TEAL   = "0F6D60"   # 表头主色
DARK   = "15312E"   # 深色文字
MINT   = "DCEFE6"   # 薄荷填充
ORANGE = "E4764D"   # 强调
SOFT   = "F7F7F3"   # 柔和底色
LINE   = "DCE6E0"   # 分隔线

wb = Workbook()
wb.remove(wb.active)   # 删掉默认的空 sheet


def add_sheet(name, headers, rows, widths):
    """
    建一个「可直接交付」的 sheet。

    做的事：冻结首行、关网格线、表头着色加粗、
    正文自动换行 + 底部分隔线、注册成 Excel 表格
    （带条纹样式，筛选/排序开箱可用）。
    """
    ws = wb.create_sheet(name)
    ws.freeze_panes = "A2"                      # 冻结表头
    ws.sheet_view.showGridLines = False         # 关网格线

    ws.append(headers)
    for row in rows:
        ws.append(row)

    # 表头：实心填充 + 白字加粗 + 居中 + 自动换行
    for cell in ws[1]:
        cell.fill = PatternFill("solid", fgColor=TEAL)
        cell.font = Font(color="FFFFFF", bold=True)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # 正文：白底 + 顶端对齐 + 自动换行 + 底部分隔线
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.fill = PatternFill("solid", fgColor="FFFFFF")
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = Border(bottom=Side(style="thin", color=LINE))

    ws.row_dimensions[1].height = 30

    # 列宽：chr(64+i) 是 A/B/C…，够用到 26 列
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[chr(64 + i)].width = width

    # 注册成 Excel 表格对象 → 自带条纹 + 筛选箭头
    ref = f"A1:{chr(64 + len(headers))}{max(2, ws.max_row)}"
    table = Table(displayName=f"T{len(wb.sheetnames)}", ref=ref)
    table.tableStyleInfo = TableStyleInfo(
        name="TableStyleMedium2",
        showRowStripes=True,
        showColumnStripes=False,
    )
    ws.add_table(table)
    return ws


add_sheet(
    "团队分工",
    ["角色", "成员姓名", "年级", "完整专业名称", "核心职责", "本周可交付物", "证据位置", "状态"],
    [
        ["项目负责人", "待填写", "待填写", "外国语学院翻译专业", "路演场景设计、双语 Rubric、用户访谈统筹、答辩", "路演 Rubric v1、2 次访谈纪要、答辩讲稿", "待填写", "进行中"],
        ["技术负责人", "待填写", "待填写", "计算机专业（完整名称待确认）", "浏览器录音、前端迭代、转写方案评估、试点数据整理", "语音页面 v0.2、测试问题单、技术说明", "待填写", "进行中"],
        ["内容与测评成员", "待填写", "待填写", "外国语学院英语专业", "英文路演素材、示范表达、双语内容校对", "英文路演题库、示范样例、校对记录", "待填写", "待开始"],
        ["用户研究与运营成员", "待填写", "待填写", "外国语学院英语专业", "问卷、访谈、试点招募、视频和材料归档", "问卷链接、试点名单、视频分镜", "待填写", "待开始"],
    ],
    [18, 14, 10, 28, 34, 34, 22, 12],
)

add_sheet(
    "试用记录",
    ["匿名编号", "日期", "年级/专业", "有无路演经历", "已同意匿名使用", "基线录音", "训练任务", "复练录音", "主要变化", "可用性问题", "证据文件/截图"],
    [[f"P-{i:02d}", "待填写", "待填写", "待填写", "是/否", "待完成", "待完成", "待完成", "只写真实观察", "待填写", "待填写"] for i in range(1, 9)],
    [13, 13, 22, 16, 18, 16, 16, 16, 28, 28, 28],
)

add_sheet(
    "访谈记录",
    ["匿名编号", "日期", "受访者场景", "最难说清的具体事件", "原话摘录", "当前替代办法", "产品启发", "访谈成员", "材料位置"],
    [[f"I-{i:02d}", "待填写", "待填写", "路演/课堂/面试", "待填写", "待填写", "待填写", "待填写", "待填写"] for i in range(1, 9)],
    [13, 13, 17, 32, 38, 26, 30, 16, 24],
)

add_sheet(
    "问卷汇总",
    ["采集日期", "指标", "题目来源", "总样本", "选择人数", "比例", "结论", "图表文件"],
    [
        ["待填写", "有竞赛/路演经历", "第 3 题", "待填写", "待填写", "自动/手填", "待填写", "待填写"],
        ["待填写", "最常见表达困难", "第 4 题", "待填写", "待填写", "自动/手填", "待填写", "待填写"],
        ["待填写", "愿意试用本地语音训练", "第 11 题", "待填写", "待填写", "自动/手填", "待填写", "待填写"],
    ],
    [15, 28, 15, 12, 12, 13, 30, 24],
)

add_sheet(
    "产品迭代",
    ["版本", "日期", "证据来源", "发现的问题", "决定的改动", "负责人", "改动截图/链接"],
    [
        ["v0.1", "已完成", "团队内部评审", "原文字输入作为主入口，无法体现口头表达训练", "改为浏览器本地录音优先，文字作为转写补充", "项目负责人 + 技术负责人", "voice-practice.html"],
        ["v0.2", "待填写", "问卷/访谈/试用", "待填写", "待填写", "待填写", "待填写"],
        ["v0.3", "待填写", "问卷/访谈/试用", "待填写", "待填写", "待填写", "待填写"],
    ],
    [12, 14, 22, 35, 35, 22, 28],
)

add_sheet(
    "重点项目检查",
    ["筛选维度", "需要证明什么", "当前材料", "负责人", "提交前状态", "补充证据"],
    [
        ["问题聚焦", "首期只解决大学生路演表达问题", "项目定位、语音原型、路演 Rubric", "项目负责人", "已具备", "教师或双创导师修改意见"],
        ["产品原型", "可演示且与问题直接相关", "本地录音、回放、报告、任务、复练", "技术负责人", "已具备", "真实试用录屏"],
        ["团队互补", "四人均有明确且真实产出", "团队分工表", "全体", "待补", "成员履历、过程记录、合影/会议纪要"],
        ["用户验证", "真实需求和试用反馈", "问卷与访谈提纲", "用户研究成员", "待补", "30 份问卷、5-8 次访谈、5-8 次试用"],
        ["校内价值", "可服务学校双创训练场景", "路演训练首期场景", "运营成员", "待补", "双创老师/课程教师意见或试点邀请"],
        ["材料表达", "PPT、计划书、视频口径一致", "18 页 PPT、计划书、演示脚本", "项目负责人", "进行中", "真实数据图表和 1 分钟视频"],
    ],
    [15, 31, 34, 20, 16, 35],
)

# ── 全局收尾：适应页宽打印 + 标签页着色 ──
for ws in wb.worksheets:
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.tabColor = TEAL

OUT.parent.mkdir(parents=True, exist_ok=True)
wb.save(OUT)
print(OUT)
