# 输入自己的token
token = ''
# 项目id，必填
show_id = '65fbb5419519d70001e27e6e'
# 指定场次id，不指定则默认从第一场开始遍历
session_id = '65fbb54d9a16700001818adc'  # 644fcb7dca916100017dda3d
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 1
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = 'E_TICKET'
# 座位类型
seat_plan_id = '65fbb71dfc0dc2000190d4d5'
