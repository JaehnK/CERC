import os
import csv
import datetime

class CSVcounter:
    """
    특정 폴더 안의 csv 파일들의 행의 갯수와 생성 시간을 파악해서 csv 파일로 리턴해주는 객체입니다.
    count_csv(), save_csv() 두 개의 함수로 이루어져 있습니다.
    
    Attributes:
    folder_path: csv 파일들이 존재하는 폴더를 입력
    verbose(BOOL): count_csv 실행과정을 출력하려면 True, 아니면 False를 입력  
    """
    def __init__(self, folder_path, verbose):
        self.FOLDER_PATH = folder_path
        self.verbose = verbose
        self.row_counts = []
        self.create_times = []
        self.csv_names = []
    
    def count_csv(self):
        """
        지정된 폴더 경로 내의 모든 CSV 파일을 탐색하고, 각 파일에 대한 행 수와 생성 시간을 기록합니다.
        verbose가 True인 경우, 각 파일의 이름, 행 수, 생성 시간을 출력합니다.
        """
        for file in os.listdir(self.FOLDER_PATH):
            file_path = os.path.join(self.FOLDER_PATH, file)
    
            ctime = os.path.getctime(file_path)
            ctime = datetime.datetime.fromtimestamp(ctime)
            time = ctime.strftime('%Y-%m-%d %H:%M')
            self.create_times.append(time)
            self.csv_names.append(file[:-4])

            with open(file_path, 'r', encoding = 'utf-8-sig') as f:
                csv_reader = csv.reader(f)
                row_count = sum (1 for row in csv_reader)
                row_counts.append(row_count)
                
                if self.verbose:
                    print("{}\n{}\n{}\n".format(file[:-4], row_count, time))
                    print("----" * 20)
                    
    
    def save_csv(self, output_file='csv_counts.csv'):
        """
        csv 파일들에 대한 정보를 csv 파일로 리턴합니다.
        output_file을 통해 리턴할 파일의 경로와 이름을 지정할 수 있으며, 지정하지 않을 경우
        ./csv_counts.csv로 지정합니다.
        """
        with open(output_file, 'w', newline='') as f:
            csvwriter = csv.writer(f, delimiter=',')
            csvwriter.writerow(['FileName', 'Count', 'CreatedTime'])
            for name, cnt, ctimes in zip(self.csv_names, self.row_counts, self.create_times):
                csvwriter.writerow([name, cnt, ctimes])


folder_path = 'FOLDER_PATH'
count = CSVcounter(folder_path = folder_path, verbose = True)
count.count_csv()
count.save_csv()

