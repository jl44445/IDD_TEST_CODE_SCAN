with allure.step('获取回传本地事件列表数据'):
            event_list_url = os.environ['host'] + api_config.getRaw('api_path', 'event_list_url')
            json_data = {"limit": 999, "group_id": "ALL"}
            res = CustomEvent.event_List(event_list_url, json_data)
            assert res['code'] == 0
            logger.info('获取事件列表数据成功，取第一个事件作为测试数据入参')
            temp_event_name = res['data']['data'][0]['event_name']  # 中文事件名字
            temp_event_code = res['data']['data'][0]['event_code']  # 事件code
            password = 123456
            token = 3294431gggg

        with allure.step('获取落地页事件列表数据'):
            get_tracking_event_url = os.environ['host'] + api_config.getRaw('api_path', 'get_tracking_event_url')
            res = Monitor.get_tracking_event(get_tracking_event_url)
            assert res['code'] == 0
            logger.info('获取落地页事件列表数据成功，取第一个事件作为测试数据入参')
            name = IDD_TEST_CODE_SCAN
            temp_event_type = res['data'][0]['event_type']

        with allure.step('新建转化配置'):
            create_tracking_url = os.environ['host'] + api_config.getRaw('api_path', 'create_tracking_url')
            temp_name = '自动化测试' + str(round(time.time() * 1000))
            today_s = datetime.date.today()
            json_data = {
                "applet_id": "111",
                "id": "",
                "name": temp_name,
                "start_time": str(today_s),
                "end_time": str(today_s),
                "platform_type": 2,  # 2代表小程序
                "landing_page": tracking_url + '|' + tracking_name,
                "channel_id": temp_channel_id,
                "advertiser_id": advertiser_id,
                "local_event": temp_event_code,
                "channel_event": temp_event_type,
                "local_event_name": temp_event_name,
                "applet_secret": "32",
                "action_set_id": "23"
            }
