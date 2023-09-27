import pytest;
import  math;
def evaluate_quality(fruit, kg):
  """
  Đánh giá chất lượng nông sản dựa trên trọng lượng

  Args:
    fruit: Loại quả, có thể là 'g' (bưởi) hoặc 'w' (dưa hấu)
    kg: Trọng lượng quả (kg)

  Returns:
    Chuỗi mô tả chất lượng quả
  """

  global result
  if fruit == 'g':
    if kg >= 0:
      if kg < 1.2:
        result = 'nhỏ'
      elif kg < 2.5:
        result = 'trung bình'
      elif kg <= 5:
        result = 'to'
    else:
      result = 'invalid'
  elif fruit == 'w':
    if kg >= 0:
      if kg < 2.5:
        result = 'nhỏ'
      elif kg < 4:
        result = 'trung bình'
      elif kg <= 5:
        result = 'to'
    else:
      result = 'invalid'
  else:
    result = 'invalid'
  return result

@pytest.mark.parametrize('fruit, kg, expected', [
  ('g', -5, 'invalid'),
  ('g', 1, 'nhỏ'),
  ('g', 2.32, 'trung bình'),
  ('g', 2.5, 'to'),
  ('g', 4.5, 'to'),
  ('g', 26, 'invalid'),
  ('w', -3000, 'invalid'),
  ('w', 0.5, 'nhỏ'),
  ('w', 1.83343535553, 'nhỏ'),
  ('w', 3, 'trung bình'),
  ('w', 5, 'to'),
  ('w', math.inf, 'invalid')
])

def test_evaluate_quality(fruit, kg, expected):
  actual = evaluate_quality(fruit, kg)
  assert actual == expected
