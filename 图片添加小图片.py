import cv2

class Change():
	def __init__(self,head_img):
		self.head_img = head_img
	def make(self):
		try:
			head_img = self.head_img
			# 读取头像和国旗图案
			img_head = cv2.imread(head_img)
			img_flag = cv2.imread('add.png')
			# 获取头像和国旗图案宽度
			w_head, h_head = img_head.shape[:2]
			w_flag, h_flag = img_flag.shape[:2]
			# 计算图案缩放比例

			scale = w_head / w_flag / 4
			# 缩放图案

			img_flag = cv2.resize(img_flag, (0, 0), fx = scale, fy = scale)
			w_flag, h_flag = img_flag.shape[:2]
			for c in range(0, 3):
				img_head[w_head - w_flag:, h_head - h_flag:, c] = img_flag[:, :, c]

			cv2.imwrite(head_img.split('.')[0] + '.jpg', img_head)
			print(head_img.split('.')[0] + '.jpg')
			return 'success'
		except Exception as e:
			pass

Change('workspace_2_hires.jpg').make()
