def test_consul_members(host):
    assert host.check_output("consul members -http-addr=http://127.0.0.1:4440 list|grep 'alive.*client'|wc -l") == "2"
