def test_consul_members(host):
    assert host.check_output("consul members -http-addr=http://127.0.0.1:4444 list|grep 'alive.*server'|wc -l") == "3"
