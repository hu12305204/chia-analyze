# Github actions template config.
oses = ["ubuntu", "macos"]
root_test_dirs = ["blockchain", "clvm", "core", "generator", "pools", "simulation", "wallet"]

# Defaults are conservative.
parallel = False
checkout_blocks_and_plots = True
install_timelord = True
job_timeout = 30
custom_vars = ["CHECK_RESOURCE_USAGE"]
