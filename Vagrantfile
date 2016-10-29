Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
  end

  config.vm.synced_folder "script/salt/", "/srv/salt/"
  config.vm.network "private_network", ip: "192.168.50.4"

  config.vm.provision :salt do |salt|
    salt.bootstrap_options = "-P"
    salt.install_master = false
    salt.masterless = true
    salt.run_highstate = false
  end

  config.ssh.forward_agent = true
end
