# import libraries
import cv2
import pandas as pd

# load image
img_path = r"C:\Users\arif shaikh\OneDrive\Desktop\C Tutorials COURSE\.vscode\pyproject\color_detection\colorpic.jpg"
img = cv2.imread(img_path)

# importing csv as pandas dataframe
csv_path = r"C:\Users\arif shaikh\OneDrive\Desktop\C Tutorials COURSE\.vscode\pyproject\color_detection\colors.csv"
index = ["col", "col_nm", "hex", "R", "G", "B"]
csv = pd.read_csv(csv_path, names=index, header=None)

# Global Var
clicked = False
r = g = b = x_pos = y_pos = 0

# col matching based on min distance
def get_col_nm(R, G, B):
    minimum = 8000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "col_nm"]
    return cname


# x,y coordinates on mouse right double click
def codinates(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image_color_detetction')
cv2.setMouseCallback('image_color_detetction', codinates)

while True:

    cv2.imshow("image_color_detetction", img)
    if clicked:

        # Calculate center of image
        height, width, _ = img.shape
        center_x, center_y = int(width/2), int(height/2)

        # Set rectangle coordinates with offset
        rect_width, rect_height = 730, 40
        rect_x1, rect_y1 = center_x-int(rect_width/2), center_y-int(rect_height/2)
        rect_x2, rect_y2 = rect_x1+rect_width, rect_y1+rect_height

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (rect_x1, rect_y1), (rect_x2, rect_y2), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_col_nm(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # Calculate text position with offset
        text_offset_x, text_offset_y = 20, 8
        text_x, text_y = center_x-int(cv2.getTextSize(text, 2, 0.8, 2)[0][0]/2)+text_offset_x, center_y+int(cv2.getTextSize(text, 2, 0.8, 2)[0][1]/2)+text_offset_y

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (text_x, text_y), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)


        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (text_x, text_y), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
