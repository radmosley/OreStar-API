from django.core.management.base import BaseCommand
from ...models import oreStarData
import csv


class Command(BaseCommand):
    help = 'Load collected CSV files into database'

    def handle(self, *args, **kwargs):
        with open('./files/XcelCNESearch.csv', newline='') as csvfile:
            fieldnames = [ 
                'Trans Id', 
                'Original Id',
                'Tran Date',
                'Tran Status',
                'Filer',
                'Contributor/Payee',
                'Sub Type',
                'Amount',
                'Aggregate Amount',
                'Contributor/Payee Committee ID',
                'Filer Id',
                'Attest By Name',
                'Attest Date',
                'Review By Name',
                'Review Date',
                'Due Date',
                'Occptn Ltr Date',
                'Pymt Sched Txt',
                'Purp Desc',
                'Intrst Rate',
                'Check Nbr',
                'Tran Stsfd Ind',
                'Filed By Name',
                'Filed Date',
                'Addr book Agent Name',
                'Book Type',
                'Title Txt',
                'Occptn Txt',
                'Emp Name',
                'Emp City',
                'Emp State',
                'Employ Ind',
                'Self Employ Ind',
                'Addr Line1',
                'Addr Line2',
                'City',
                'State',
                'Zip',
                'Zip Plus Four',
                'County',
                'Purpose Codes'
                ]
            spreadsheet = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in csvfile:
                t = oreStarData( 
                    tran_id = row['Tran Id'], 
                    original_id =row['Original Id'],
                    tran_date= row['Tran Date'], 
                    tran_status =row['Tran Status'],
                    filer =row['Filer'], 
                    payee =row['Contributor/Payee'], 
                    subtype =row['Sub Type'],
                    amount =row['Amount'], 
                    agg_amount = row['Aggregate Amount'], 
                    payee_id = row['Contributor/Payee Committee ID'], 
                    filer_id =row['Filer Id'], 
                    attest_by_name =row['Attest By Name'], 
                    attest_date =row['Attest Date'], 
                    review_by_name =row['Review By Name'], 
                    review_date = row['Review Date'],
                    due_date = row['Due Date'],
                    occptn_ltr_date = row['Occptn Ltr Date'],
                    payment_text =row['Pymt Sched Txt'], 
                    purps_desc =row['Purp Desc'], 
                    intrst_rate =row['Intrst Rate'], 
                    check_numb =row['Check Nbr'], 
                    trans_status_ind =row['Tran Stsfd Ind'], 
                    file_by_name =row['Filed By Name'], 
                    file_date = row['Filed Date'],
                    addr_book_agent =row['Addr book Agent Name'], 
                    book_type =row['Book Type'], 
                    title_txt = row['Title Txt'], 
                    occptn_txt = row['Occptn Txt'], 
                    emp_name = row['Emp Name'], 
                    emp_city = row['Emp City'], 
                    emp_state = row['Emp State'], 
                    emploeed_ind = row['Employ Ind'], 
                    self_employee_ind = row['Self Employ Ind'], 
                    addr_line_1 = row['Addr Line1'], 
                    addr_line_2 = row['Addr Line2'], 
                    city = row['City'], 
                    state = row['State'], 
                    zipcode = row['Zip'], 
                    zipplus = row['Zip Plus Four'], 
                    county = row['County'], 
                    purpose_code = row['Purpose Codes']
                )
                t.save()
                self.stdout.write('{} loaded'.format(row['Trans Id']))