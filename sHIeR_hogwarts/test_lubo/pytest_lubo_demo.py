

import pytest
import yaml

class TestClass:
  @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
  def testclass(self,env):
      if "test" in env:
          print("这是测试环境")
          print("测试环境IP是：",env["test"])