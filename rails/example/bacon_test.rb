require 'minitest/autorun'

class Bacon
  def self.saved?
  end
end

class BaconTest < Minitest::Test
  def test_saved
    assert Bacon.saved?, "Our bacon was not saved"
  end
end
