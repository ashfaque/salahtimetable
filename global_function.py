
# from django.shortcuts import render
from django.conf import settings
# from rest_framework import mixins
# from rest_framework import filters
from datetime import datetime, timedelta, date
# import collections
# from rest_framework.parsers import FileUploadParser
# from django_filters.rest_framework import DjangoFilterBackend
import os
import platform
# from django.http import JsonResponse
# from decimal import Decimal
#from django.db.models import Q
from custom_exception_message import *
from decimal import *
# import math
# from django.contrib.auth.models import *
# from django.db.models import F
# from django.db.models import Count
# from core.models import *
# from etask.models import *
# from users.models import TCoreUserDetail, UserTempReportingHeadMap
# from attendance.models import AttendenceMonthMaster, JoiningApprovedLeave
# import re
# from dateutil.relativedelta import relativedelta
# import platform

from redis_handler import pub as email_pub
from django.template import Context, Template
from mailsend.models import MailHistory, MailTemplate, MailICSMapping
import json
# from employee_leave_calculation import grace_calculation, roundOffLeaveCalculationUpdate
# import numpy as np
# import pandas as pd


# def userdetails(user):
#     # print(type(user))
#     f_name_l_name = None
#     if isinstance(user, (int)):
#         name = User.objects.filter(id=user)
#         for i in name:
#             # print("i",i)
#             f_name_l_name = i.first_name + " " + i.last_name
#             # print("f_name_l_name",f_name_l_name)
#     elif isinstance(user, (str)):
#         # print(user ,"str")
#         name = User.objects.filter(username=user)
#         for i in name:
#             # print("i",i)
#             f_name_l_name = i.first_name + " " + i.last_name
#             # print("f_name_l_name",f_name_l_name)
#     else:
#         f_name_l_name = None

#     return f_name_l_name


# def designation(designation):
#     if isinstance(designation, (str)):
#         desg_data = TCoreUserDetail.objects.filter(cu_user__username=designation)
#         if desg_data:
#             for desg in desg_data:
#                 return desg.designation.cod_name
#         else:
#             return None
#     elif isinstance(designation, (int)):
#         desg_data = TCoreUserDetail.objects.filter(cu_user=designation)
#         if desg_data:
#             for desg in desg_data:
#                 return desg.designation.cod_name
#         else:
#             return None


# def department(department):
#     if isinstance(department, (str)):
#         desg_data = TCoreUserDetail.objects.filter(cu_user__username=department)
#         if desg_data:
#             for desg in desg_data:
#                 return desg.department.cd_name
#         else:
#             return None
#     elif isinstance(department, (int)):
#         desg_data = TCoreUserDetail.objects.filter(cu_user=department)
#         if desg_data:
#             for desg in desg_data:
#                 return desg.department.cd_name
#         else:
#             return None


def getHostWithPort(request, media=False):
    if os.environ.get('SERVER_GATEWAY_INTERFACE') == 'Web':
        protocol = 'https://' if request.is_secure() else 'http://'
        url = protocol+request.get_host()+'/media/' if media else protocol+request.get_host()+'/'
    else:
        url = settings.SERVER_URL+'media/' if media else settings.SERVER_URL
    return url

def getOwnHost(request):
    scheme = request.is_secure() and "https" or "http"
    return scheme+"://"+request.get_host()+"/"




# def getPathFromMediaURL(url):
#     spiltted = url.split('media/')
#     relative_path = spiltted[1]
#     path = os.path.join(settings.MEDIA_ROOT, relative_path)
#     os_name = platform.system().lower()
#     if os_name == "windows":
#         path = path.replace('/', '\\')
#     return path



# def raw_query_extract(query):

#     return query.query


# def round_calculation(days: int, leave_count: int) -> float:
#     print('days', days, ":int,", leave_count)
#     int_value = days*leave_count//365
#     frq_value = round((days*leave_count/365), 2) - int_value
#     print("int_value", int_value, "frq_value", frq_value)
#     frq_add = 0.0
#     # if frq_value < 0.25:
#     #     value = float(int_value)+frq_add
#     if frq_value >= 0.0 and frq_value <= 0.25:
#         frq_add = 0.0
#         value = float(int_value)+frq_add
#     elif frq_value >= 0.25 and frq_value <= 0.75:
#         frq_add = 0.5
#         value = float(int_value)+frq_add
#     elif frq_value > 0.75:
#         frq_add = 1.0
#         value = float(int_value)+frq_add
#     print("value", value)
#     return value


# def round_calculation_V2(days: int, leave_count: int) -> float:
#     # print('days', days,":int,", leave_count)

#     return value


# def convert24(str1):

#     # 1:56PM

#     # Checking if last two elements of time
#     # is AM and first two elements are 12
#     if str1[-2:] == "AM" and str1[:2] == "12":
#         return "00" + str1[2:-2]

#     # remove the AM
#     elif str1[-2:] == "AM":
#         # return "0"+str1[:-2]
#         return str1[:-2]

#     # Checking if last two elements of time
#     # is PM and first two elements are 12
#     elif str1[-2:] == "PM" and str1[:2] == "12":
#         print('str 1', str1[:-2])
#         return str1[:-2]

#     else:

#         # add 12 to hours and remove PM
#         return str(int(str1[:1]) + 12) + str1[1:4]


# def get_users_under_reporting_head(user=None):
#     reporting_heads = list(TCoreUserDetail.objects.filter(reporting_head=user, cu_is_deleted=False, cu_user__isnull=False).values_list('cu_user__id', flat=True))
#     temp_reporting_heads = list(UserTempReportingHeadMap.objects.filter(temp_reporting_head=user, is_deleted=False).values_list('user__id', flat=True))
#     reporting_heads.extend(temp_reporting_heads)
#     return reporting_heads


# def get_user_reporting_heads(user=None):
#     reporting_head = list(TCoreUserDetail.objects.filter(cu_user=user, cu_is_deleted=False, cu_user__isnull=False).values_list('reporting_head__id', flat=True))
#     temp_reporting_heads = list(UserTempReportingHeadMap.objects.filter(user=user, is_deleted=False).values_list('temp_reporting_head__id', flat=True))
#     reporting_head.extend(temp_reporting_heads)
#     return reporting_head


# def get_time_diff(DurationFrom, durationTo):
#     print('DurationFrom',DurationFrom,',durationTo',durationTo)
#     date_format = "%H:%M:%S"
#     durationTo = datetime.strptime(str(durationTo), date_format)
#     DurationFrom = datetime.strptime(str(DurationFrom), date_format)
#     timediff = (durationTo-DurationFrom).total_seconds()
#     hours = round(timediff / 3600, 2)
#     print('hours',hours)
#     return hours

# def get_time_diff_wo_sec(DurationFrom, durationTo):
#     #print('DurationFrom',DurationFrom,',durationTo',durationTo)
#     date_format = "%H:%M"
#     durationTo = datetime.strptime(str(durationTo), date_format)
#     DurationFrom = datetime.strptime(str(DurationFrom), date_format)
#     timediff = (durationTo-DurationFrom)
#     #print('timediff',timediff)
#     hours = str(timediff).split(':')[0]
#     mins = str(timediff).split(':')[1]
#     #print('hours',hours,mins)
#     #raise APIException('sadsad')
#     return int(hours),int(mins)

#     # date_input = str(date_input)[0:10]
#     # if output_format:
#     #     date_input_after_conversion = datetime.strftime(datetime.strptime(date_input,'%Y-%m-%d'),output_format)
#     # else:
#     #     date_input_after_conversion = datetime.strftime(datetime.strptime(date_input,'%Y-%m-%d'),'%d-%m-%Y')
#     # return date_input_after_conversion


# def get_pagination_offset(page=1, page_count=10):
#     return slice(page_count*(page-1), page*page_count)


# def create_appointment(reporting_dates=[]):
#     reporting_ids = [rd.id for rd in reporting_dates]
#     reporting_dates_query = ETaskReportingDates.objects.filter(id__in=reporting_ids)
#     for reporting_date_obj in reporting_dates_query:
#         reporting_date = reporting_date_obj.reporting_date
#         reporting_end_date = reporting_date_obj.reporting_end_date if reporting_date_obj.reporting_end_date else reporting_date
#         if reporting_date_obj.is_manual_time_entry:
#             task = EtaskTask.objects.get(id=reporting_date_obj.task)
#             data = dict()
#             data['facilitator'] = 2
#             data['appointment_subject'] = task.task_subject
#             data['start_date'] = reporting_date
#             data['end_date'] = reporting_end_date
#             data['start_time'] = reporting_date.time()
#             data['end_time'] = reporting_end_date.time()
#             data['Appointment_status'] = 'ongoing'
#             data['owned_by'] = reporting_date_obj.created_by
#             data['created_by'] = reporting_date_obj.created_by
#             data['location'] = ''
#             apointment_create = EtaskAppointment.objects.create(**data)

#             subassign_log = EtaskTaskSubAssignLog.objects.filter(task=task, assign_from=apointment_create.owned_by, is_deleted=False).first()
#             assign_to = subassign_log.sub_assign if subassign_log else task.assign_to

#             mail = {'name': assign_to.get_full_name(), 'email': assign_to.cu_user.cu_alt_email_id}
#             mail_list = [mail, {'name': apointment_create.owned_by.get_full_name(), 'email': apointment_create.owned_by.cu_user.cu_alt_email_id}]
#             EtaskInviteEmployee.objects.create(appointment=apointment_create, user=assign_to)

#             s_date = reporting_date.strftime("%Y%m%dT%H%M%S")
#             e_date = reporting_end_date.strftime("%Y%m%dT%H%M%S")
#             invitation_from = '{} ({})'.format(apointment_create.owned_by.get_full_name(), apointment_create.owned_by.cu_user.cu_alt_email_id)
#             invited_to = '{} ({})'.format(assign_to.get_full_name(), assign_to.cu_user.cu_alt_email_id)
#             ics_data = """BEGIN:VCALENDAR
# VERSION:2.0
# CALSCALE:GREGORIAN
# BEGIN:VEVENT
# SUMMARY:Appointment of {}
# DTSTART;TZID=Asia/Kolkata:{}
# DTEND;TZID=Asia/Kolkata:{}
# LOCATION:Shyam Tower,Kolkata-700091
# DESCRIPTION: Appointment Invitation From-> {}  Invited People-> {}
# STATUS:CONFIRMED
# SEQUENCE:3
# BEGIN:VALARM
# TRIGGER:-PT10M
# DESCRIPTION:Pickup Reminder
# ACTION:DISPLAY
# END:VALARM
# END:VEVENT
# END:VCALENDAR""".format(apointment_create.appointment_subject, s_date, e_date, invitation_from, invited_to)

            # #===============================================#
            # for mail_dict in mail_list:
            #     if mail_dict['email']:
            #         mail_data = {
            #             "recipient_name": mail_dict['name'],  # modified by manas Paul 21jan20
            #             "appointment_subject": apointment_create.appointment_subject,
            #             "facilitator_name": apointment_create.owned_by.get_full_name(),
            #             "location": 'NA',
            #             "start_date": reporting_date.date(),
            #             "end_date": reporting_end_date.date(),
            #             "start_time": reporting_date.time(),
            #             "end_time": reporting_end_date.time(),
            #             "internal_invitees": [mail],
            #             "external_invitees": [],
            #             "invitee_count": 1
            #         }
            #         send_mail('ETAP', mail_dict['email'], mail_data, ics_data)


def send_mail(code, user_email, mail_data, cc=None, bcc=None, ics='', final_sub='',subject=''):
    if bcc is None:
        bcc = list()
    if cc is None:
        cc = list()
    send_mail_list(code, [user_email], mail_data, cc, bcc, ics, final_sub,subject)


def send_mail_list(code, user_email_list, mail_data, cc=None, bcc=None, ics='', final_sub='',subject=''):
    if bcc is None:
        bcc = list()
    if cc is None:
        cc = list()
    mail_content = MailTemplate.objects.get(code=code)
    if subject:
        subject = subject
    else:
        subject = mail_content.subject + final_sub
        
    template_variable = mail_content.template_variable.split(",")
    html_content = Template(mail_content.html_content)
    match_data_dict = {}
    for data in template_variable:
        if data.strip() in mail_data:
            match_data_dict[data.strip()] = mail_data[data.strip()]
    if match_data_dict:
        context_data = Context(match_data_dict)
        html_content = html_content.render(context_data)
    #print('html_content',html_content)
    entry = MailHistory()
    entry.code = code
    entry.recipient_list = json.dumps(user_email_list)
    ## Cc and Bcc are added
    entry.cc = json.dumps(cc)
    entry.bcc = json.dumps(bcc)
    entry.body = html_content
    entry.subject = subject
    entry.attachment = ics
    l = entry.save()
    success, msg = email_pub.publish('salah_email', [entry.id])


## to handle sequence and uid in ICS files
# def get_uid_sequence_for_event(email_id, module, event_id):
#     email_id = str(email_id).lower()
#     instance = MailICSMapping.objects.filter(module=module, event_id=event_id, email=email_id)
#     if instance:
#         instance = instance[0]
#         instance.sequence += 1
#         instance.save()
#     else:
#         import uuid
#         instance = MailICSMapping()
#         instance.uuid = uuid.uuid4()
#         instance.module = module
#         instance.email = email_id
#         instance.sequence = 0
#         instance.event_id = event_id
#         instance.save()
#     return (instance.sequence, instance.uuid)


# # for writing excel using xlsxwriter
# def worksheet_write(worksheet, cell_width_map, row_idx, col_idx, val, cell_format):
#     worksheet.write(row_idx, col_idx, val, cell_format)
#     width = 8
#     if len(str(val)) > 8:
#         width = len(str(val)) * 0.9
#     if col_idx in cell_width_map and cell_width_map[col_idx] > width:
#         width = cell_width_map[col_idx]
#     cell_width_map[col_idx] = width
#     worksheet.set_column(col_idx, col_idx, width=cell_width_map[col_idx])


# def worksheet_merge_range(worksheet, cell_height_map, row_idx1, col_idx1, row_idx2, col_idx2, val, format):
#     worksheet.merge_range(row_idx1, col_idx1, row_idx2, col_idx2, val, format)
#     height = 15
#     for c in str(val):
#         if c == '\n':
#             height += 16
#     if row_idx1 in cell_height_map and cell_height_map[row_idx1] > height:
#         height = cell_height_map[row_idx1]
#     cell_height_map[row_idx1] = height
#     worksheet.set_row(row_idx1, height=cell_height_map[row_idx1])


# def worksheet_merge_range_by_width(worksheet, cell_width_map, row_idx1, col_idx1, row_idx2, col_idx2, val, format):
#     worksheet.merge_range(row_idx1, col_idx1, row_idx2, col_idx2, val, format)
#     width = 8
#     if len(str(val)) > 8:
#         width = len(str(val)) * 0.9
#     col_idx = col_idx1
#     if col_idx in cell_width_map and cell_width_map[col_idx] > width:
#         width = cell_width_map[col_idx]
#     cell_width_map[col_idx] = width
#     worksheet.set_column(col_idx, col_idx, width=cell_width_map[col_idx])

# def get_last_day_of_month(datetime_obj):
#     # get close to the end of the month for any day, and add 4 days 'over'
#     next_month = datetime_obj.replace(day=28) + timedelta(days=4)
#     # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
#     return next_month - timedelta(days=next_month.day)

# def get_current_financial_year_details():
#     c_date = datetime.now()
#     #c_date = '2018-01-01'
#     current_financial_year_details = AttendenceMonthMaster.objects.filter(
#             year_start_date__date__lte=c_date,
#             year_end_date__date__gte=c_date,
#             is_deleted=False
#             ).values('month_start__date','month_end__date','year_start_date__year','year_end_date__year')
#     if  current_financial_year_details:
#         return current_financial_year_details.first()
#     else :

#         raise APIException({'result':{'status':404,'msg':'Current Financial Year Details Not Found'}})
    

# def employee_lave_allocation(usr_obj):
#     if str(usr_obj.salary_type.st_code) == "AA":
#         usr_obj.granted_el = float(0)
#         usr_obj.granted_leaves_cl_sl = float(0)
#         usr_obj.save()
#         granted_cl = 0
#         granted_sl = 0
#         granted_el = 0
#     elif str(usr_obj.salary_type.st_code) == "BB":
#         usr_obj.granted_el = float(15)
#         usr_obj.granted_leaves_cl_sl = float(10)
#         usr_obj.save()
#         granted_cl = 10
#         granted_sl = 0
#         granted_el = 15
#     elif str(usr_obj.salary_type.st_code) == "FF":
#         usr_obj.granted_el = float(15)
#         usr_obj.granted_leaves_cl_sl = float(16)
#         usr_obj.save()
#         granted_cl = 16
#         granted_sl = 0
#         granted_el = 15
#     elif str(usr_obj.salary_type.st_code) in ["CC", "DD"]:
#         usr_obj.granted_el = float(15)
#         usr_obj.granted_leaves_cl_sl = float(17)
#         usr_obj.save()
#         granted_cl = 10
#         granted_sl = 7
#         granted_el = 15
#     elif str(usr_obj.salary_type.st_code) == "EE":
#         usr_obj.granted_el = float(15)
#         usr_obj.granted_leaves_cl_sl = float(16)
#         usr_obj.save()
#         granted_cl = 10
#         granted_sl = 6
#         granted_el = 15

#     else:
#         granted_el = 0
#         granted_cl = 0
#         granted_sl = 0

#     usr_obj.granted_el = granted_el
#     usr_obj.granted_cl = granted_cl
#     usr_obj.granted_sl = granted_sl
#     usr_obj.save()
#     joining_date = usr_obj.joining_date
#     joining_year = joining_date.year
#     # print('joining_year',joining_year)
#     today = datetime.now()
#     current_month = AttendenceMonthMaster.objects.get(
#         month_start__date__lte=today,
#         month_end__date__gte=today, is_deleted=False)
#     year_start_date = current_month.year_start_date
#     year_end_date = current_month.year_end_date
#     joining_date = usr_obj.joining_date
#     print(joining_date)
#     from_date = year_start_date
#     to_date = year_end_date
#     print(from_date, to_date)
#     is_joining_year = False
#     if joining_date > from_date:
#         is_joining_year = True
#         from_date = joining_date
#     leave_filter = {}
#     print("from date????????", from_date)
#     print("to date????????", to_date)

#     attendenceMonthMaster = AttendenceMonthMaster.objects.filter(month_end__date__gte=from_date,
#                                                                  month_end__date__lte=to_date,
#                                                                  is_deleted=False).values('id',
#                                                                                           'grace_available',
#                                                                                           'year_start_date',
#                                                                                           'year_end_date',
#                                                                                           'month',
#                                                                                           'month_start',
#                                                                                           'month_end',
#                                                                                           'days_in_month',
#                                                                                           'payroll_month')
#     print("attendenceMonthMaster-----------", attendenceMonthMaster)
#     user = usr_obj.cu_user
#     if attendenceMonthMaster:
#         available_grace = grace_calculation(joining_date.date(), attendenceMonthMaster)
#         # print('available_grace',available_grace)
#         year_end_date = attendenceMonthMaster[0]['year_end_date'].date()
#         month_start = attendenceMonthMaster[0]['month_start'].date()
#         # total_days = ((year_end_date - joining_date).days) + 1
#         total_days = ((to_date - from_date).days) + 1
#         # print('total_days',total_days)
#         cl, al, el, sl = 0, 0, 0, 0
#         if user.cu_user.salary_type:
#             if user.cu_user.salary_type.st_code in ['FF', 'EE']:
#                 al = round_calculation(total_days, (granted_cl + granted_sl + granted_el))
#             elif user.cu_user.salary_type.st_code in ['CC', 'DD']:
#                 cl = round_calculation(total_days, granted_cl)
#                 sl = round_calculation(total_days, granted_sl)
#                 el = round_calculation(total_days, granted_el)
#             elif user.cu_user.salary_type.st_code in ['BB']:
#                 cl = round_calculation(total_days, granted_cl)
#                 # sl = round_calculation(total_days, granted_sl)
#                 el = round_calculation(total_days, granted_el)
#             else:
#                 pass

#         # leave_confirm = round_calculation(total_days, (granted_cl + granted_sl + granted_el))
#         leave_confirm = round_calculation(total_days, (granted_cl + granted_sl + granted_el))
#         # leave_part_2_not_confirm = round_calculation(total_days, (granted_cl + granted_sl))
#         # leave_part_2_not_confirm = round_calculation(total_days, (granted_cl + granted_sl + granted_el))
#         if user.cu_user.salary_type:
#             if user.cu_user.salary_type.st_code in ['FF', 'EE']:
#                 # leave_filter['cl'] = leave_confirm // 2
#                 # leave_filter['sl'] = leave_confirm - (leave_confirm // 2)
#                 leave_filter['cl'] = float(0)
#                 leave_filter['sl'] = float(0)
#                 leave_filter['el'] = float(0)
#                 leave_filter['al'] = leave_confirm
#                 leave_filter['granted_leaves_cl_sl'] = leave_confirm
#             else:
#                 leave_filter['granted_leaves_cl_sl'] = round_calculation(total_days,
#                                                                          (granted_cl + granted_sl))

#                 if granted_cl:
#                     leave_filter['cl'] = round_calculation(total_days, granted_cl)
#                 else:
#                     leave_filter['cl'] = float(0)
#                 if granted_sl:
#                     leave_filter['sl'] = round_calculation(total_days, granted_sl)
#                 else:
#                     leave_filter['sl'] = float(0)
#                 if granted_el:
#                     leave_filter['el'] = round_calculation(total_days, granted_el)
#                 else:
#                     leave_filter['el'] = float(0)
#         # leave_filter['granted_leaves_cl_sl'] = round_calculation(total_days, (granted_cl + granted_sl))
#         # if granted_el:
#         #     leave_filter['el'] = round_calculation(total_days, granted_el)
#         # else:
#         #     leave_filter['el'] = float(0)
#         # leave_filter['cl'] = cl
#         # leave_filter['sl'] = sl
#         users = [user.id]
#         roundOffLeaveCalculationUpdate(users, attendenceMonthMaster,
#                                        leave_confirm, leave_confirm,
#                                        total_days,
#                                        year_end_date, attendenceMonthMaster[0]['month_start'], joining_date,
#                                        cl, sl, el, al, is_joining_year)
#     else:
#         available_grace = None
#     if available_grace:
#         if attendenceMonthMaster[0]['year_start_date'].date() < joining_date.date():
#             JoiningApprovedLeave.objects.get_or_create(employee=user,
#                                                        year=joining_year,
#                                                        month=attendenceMonthMaster[0]['month'],
#                                                        **leave_filter,
#                                                        first_grace=available_grace,
#                                                        created_by=user,
#                                                        owned_by=user
#                                                        )
#         else:
#             JoiningApprovedLeave.objects.get_or_create(employee=user,
#                                                        year=joining_year,
#                                                        month=attendenceMonthMaster[0]['month'],
#                                                        **leave_filter,
#                                                        first_grace=available_grace,
#                                                        created_by=user,
#                                                        owned_by=user
#                                                        )
#     else:
#         JoiningApprovedLeave.objects.get_or_create(employee=user,
#                                                    year=joining_year,
#                                                    month=attendenceMonthMaster[0]['month'],
#                                                    **leave_filter,
#                                                    first_grace=available_grace,
#                                                    created_by=user,
#                                                    owned_by=user
#                                                    )

#     return True


# def create_file_path(base_path='', file_name=''):
#     if os.path.isdir(base_path):
#         file_path_name = '{}/{}'.format(base_path, file_name)
#     else:
#         os.makedirs(base_path)
#         file_path_name = '{}/{}'.format(base_path, file_name)
#     return file_path_name

# ## [Added xlsxwriter]
# def download_url_generator(request, data=[], base_path='', extension_type='xlsx', file_name='', columns=[], headers=[],sl=False,index_label='#',blank_value_replace_with=''):
#     #print('index_label',index_label)
#     file_path_name = create_file_path(base_path=base_path, file_name=file_name)
#     file_path = settings.MEDIA_ROOT_EXPORT + file_path_name
#     writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

#     if not data:
#         final_df = pd.DataFrame(data,columns=headers)
#         final_df.to_excel(writer, sheet_name='Sheet1', header=False)
#         workbook  = writer.book
#         header_fmt = workbook.add_format({'bg_color':'green','font_color':'white'})
#         header_sl_fmt = workbook.add_format({'bg_color':'#3366FF','font_color':'white','align':'center'})
#         worksheet = writer.sheets['Sheet1']
#         for col_num, value in enumerate(final_df.columns.values):
#             worksheet.write(0, col_num + 1, value, header_fmt)
#         worksheet.write('A1', index_label, header_sl_fmt) # For sl_no cell formatting
#         #writer.save()
#     else:
#         if columns:
#             df = pd.DataFrame.from_records(data)[columns]
#         else:
#             df = pd.DataFrame.from_records(data)

#         df.replace(to_replace=['None',' ',[None]], value=blank_value_replace_with, inplace=True) # None value replace by
#         df.replace(to_replace=["False"], value='no', inplace=True) # False value replace by 'no' Text
#         df.replace(to_replace=["True"], value='yes', inplace=True) # True value replace by 'yes' Text
        
#         if sl:
#             df.index = np.arange(1, len(df) + 1) # starting index from 1

#         if extension_type == 'xlsx':
#             if sl:
#                 df.to_excel(writer, sheet_name='Sheet1', index=True, header=headers,index_label = index_label)
#             else:
#                 df.to_excel(writer, sheet_name='Sheet1', index=None, header=headers)

#         elif extension_type == 'csv':
#             if sl:
#                 df.to_csv(writer, sheet_name='Sheet1', index=True, header=headers, index_label = index_label)
#             else:
#                 df.to_csv(writer, sheet_name='Sheet1', index=None, header=headers)
#         else:
#             if sl:
#                 df.to_excel(writer, sheet_name='Sheet1', index=True, header=headers, index_label = index_label)
#             else:
#                 df.to_excel(writer, sheet_name='Sheet1', index=None, header=headers)
                
#         # Get the dimensions of the dataframe.
#         (max_row, max_col) = df.shape
#         workbook  = writer.book
#         worksheet = writer.sheets['Sheet1']
#         # Set the autofilter.
#         worksheet.autofilter(0, 1, max_row, max_col) # For autofilter set
#         worksheet.freeze_panes(1,1) # For freeze header

#         text_wrap_format = workbook.add_format({'text_wrap': True,'align':'center'})
#         worksheet.set_column(1,max_col,25,text_wrap_format) # For cell width set and text wrap set

#         header_fmt = workbook.add_format({'bg_color':'green','font_color':'white','align':'center'})
#         header_sl_fmt = workbook.add_format({'bg_color':'#3366FF','font_color':'white','align':'center'})
        
#         for col_num, value in enumerate(headers):
#             if sl:
#                 worksheet.write(0, col_num + 1 , value, header_fmt) # For header cell formatting
#             else:
#                 worksheet.write(0, col_num , value, header_fmt) # For header cell formatting

#         if sl:
#             worksheet.write('A1', index_label, header_sl_fmt) # For sl_no cell formatting

#     writer.save()
#     url = getHostWithPort(request) + file_path_name if file_path_name else None
#     return url


# def response_on_off_modified(response):
#     data_dict = {}
#     if 'results' in response.data:
#         data_dict = response.data
#     else:
#         data_dict['results'] = response.data

#     if response.data:
#         data_dict['request_status'] = 1
#         data_dict['msg'] = settings.MSG_SUCCESS
#     elif len(response.data) == 0:
#         data_dict['request_status'] = 1
#         data_dict['msg'] = settings.MSG_NO_DATA
#     else:
#         data_dict['request_status'] = 0
#         data_dict['msg'] = settings.MSG_ERROR

#     return data_dict

# # function to convert string to camelCase
# def camelCase(string):
#   string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
#   return string[0].lower() + string[1:]
  
# def calculateAge(birthday):
#     birthday = datetime.strptime(str(birthday),'%Y-%m-%d')
#     today = date.today()
#     age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
#     return age

# def dateFormatting(date_input,output_format=None):
#     date_input = str(date_input)[0:10]
#     if output_format:
#         date_input_after_conversion = datetime.strftime(datetime.strptime(date_input,'%Y-%m-%d'),output_format)
#     else:
#         date_input_after_conversion = datetime.strftime(datetime.strptime(date_input,'%Y-%m-%d'),'%d-%m-%Y')
#     return date_input_after_conversion

# def get_days_count_of_the_month(year,month):
#     from calendar import monthrange
#     return monthrange(year=int(year), month=int(month))[1]


# def download_url_generator_with_merge_rows(request, data=[], base_path='', extension_type='xlsx', file_name='', columns=[], headers=[]):
#     #print('index_label',index_label)
#     if columns:
#         df = pd.DataFrame.from_records(data)[columns]
#     else:
#         df = pd.DataFrame.from_records(data)
    
#     file_path_name = create_file_path(base_path=base_path, file_name=file_name)
#     file_path = settings.MEDIA_ROOT_EXPORT + file_path_name
#     writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

#     if extension_type == 'xlsx':
#         df.to_excel(writer, sheet_name='Sheet1', index=None, header=headers)

#     elif extension_type == 'csv':
#         df.to_csv(writer, sheet_name='Sheet1', index=None, header=headers)
    
#     else:
#         df.to_excel(writer, sheet_name='Sheet1', index=None, header=headers)
            
#     # Get the dimensions of the dataframe.
#     (max_row, max_col) = df.shape
#     workbook  = writer.book
#     worksheet = writer.sheets['Sheet1']
#     # Set the autofilter.
#     #worksheet.autofilter(0, 1, max_row, max_col) # For autofilter set
#     worksheet.freeze_panes(1,1) # For freeze header

#     header_fmt = workbook.add_format({'bg_color':'green','font_color':'white','align':'center'})
    
#     for col_num, value in enumerate(headers):
#         worksheet.write(0, col_num , value, header_fmt) # For header cell formatting

#     merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 2})
#     count = 1
#     print('df',df)
#     print('df[3]',df[3])
#     for car in [df[3].unique()]:
#         print('car[0]',car[0])
#         u=df.loc[df[3]==car[0]].index.values + 1
#         if len(u) <2: 
#             pass # do not merge cells if there is only one car name
#         else:
#             # merge cells using the first and last indices
#             worksheet.merge_range(u[0], 1, u[-1], 1, df.loc[u[0],1], merge_format)
#             worksheet.merge_range(u[0], 2, u[-1], 2, df.loc[u[0],2], merge_format)
#             worksheet.merge_range(u[0], 3, u[-1], 3, df.loc[u[0],3], merge_format)
#             worksheet.merge_range(u[0], 0, u[-1], 0, count, merge_format)
#             count = count + 1

#     # for car in [df[3].unique()]:
#     #     u=df.loc[df[3]==car[0]].index.values + 1
#     #     if len(u) <2: 
#     #         pass # do not merge cells if there is only one car name
#     #     else:
#     #         # merge cells using the first and last indices
#     #         worksheet.merge_range(u[0], 3, u[-1], 3, df.loc[u[0],3], merge_format)
#     #         #worksheet.merge_range(u[0], 2, u[-1], 2, df.loc[u[0],2], merge_format)
#     #         worksheet.merge_range(u[0], 0, u[-1], 0, count, merge_format)
#     #         count = count + 1

#     writer.save()
#     url = getHostWithPort(request) + file_path_name if file_path_name else None
#     return url

# def get_sorted_by_extra_fields(self,response,field_type=None,field_name=None):

#     field_name =  field_name if field_name else self.request.query_params.get('ordering') 
#     if 'results' in response.data:
#         if '-' in field_name:
#             field_name = field_name[1:]
#             if field_type == 'float':
#                 response.data['results'] = sorted(response.data['results'], key=lambda i: float(i[field_name]) if i[field_name] else float(0),reverse=True)
#             else:
#                 response.data['results'] = sorted(response.data['results'], key=lambda i: str(i[field_name]) if i[field_name] else '',reverse=True)
#         else:
#             if field_type == 'float':
#                 response.data['results'] = sorted(response.data['results'], key=lambda i: float(i[field_name]) if i[field_name] else float(0))
#             else:
#                 response.data['results'] = sorted(response.data['results'], key=lambda i: str(i[field_name]) if i[field_name] else '')
#     else:
#         if '-' in field_name:
#             field_name = field_name[1:]
#             response.data = sorted(response.data, key=lambda i: i[field_name]if i[field_name] else '',reverse=True)
#         else:
#             response.data = sorted(response.data, key=lambda i: i[field_name] if i[field_name] else '')
#     return response

# def get_sorted_by_fields(self,response):
#     field_name =  self.request.query_params.get('ordering')
#     #print('response',response)
#     if 'results' in response:
#         if '-' in field_name:
#             field_name = field_name[1:]
#             response['results'] = sorted(response['results'], key=lambda i: str(i[field_name]) if i[field_name] else '',reverse=True)
#         else:
#             response['results'] = sorted(response['results'], key=lambda i: str(i[field_name]) if i[field_name] else '')
#     else:
#         if '-' in field_name:
#             field_name = field_name[1:]
#             response = sorted(response, key=lambda i: str(i[field_name]) if i[field_name] else '',reverse=True)
#         else:
#             response = sorted(response, key=lambda i: str(i[field_name]) if i[field_name] else '')
#     return response

# def get_start_end_date_of_current_week(input_date=None):
#     import pendulum
#     today = pendulum.instance(datetime.strptime(input_date, "%Y-%m-%d")) if input_date else pendulum.now()
#     print('today',pendulum.instance(today))
#     start = today.start_of('week')
#     #print(start.to_datetime_string())
#     end = today.end_of('week')
#     #print(end.to_datetime_string())
#     return start,end

# def download_url_generator_merge(request, data=[], base_path='', extension_type='xlsx', file_name='', columns=[], headers=[],sl=False,index_label='#',extra_header=None,extra_data_on_top=None,column_bg=None,autofilter=None):
#     #print('index_label',index_label)
#     file_path_name = create_file_path(base_path=base_path, file_name=file_name)
#     file_path = settings.MEDIA_ROOT_EXPORT + file_path_name
#     writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

#     if not data:
#         final_df = pd.DataFrame(data,columns=headers)
#         final_df.to_excel(writer, sheet_name='Sheet1', header=False)
#         workbook  = writer.book
#         header_fmt = workbook.add_format({'bg_color':'green','font_color':'white'})
#         header_sl_fmt = workbook.add_format({'bg_color':'#3366FF','font_color':'white','align':'center'})
#         worksheet = writer.sheets['Sheet1']
#         for col_num, value in enumerate(final_df.columns.values):
#             worksheet.write(0, col_num + 1, value, header_fmt)
#         worksheet.write('A1', index_label, header_sl_fmt) # For sl_no cell formatting
#         #writer.save()
#     else:
#         if columns:
#             df = pd.DataFrame.from_records(data)[columns]
#         else:
#             df = pd.DataFrame.from_records(data)
        
#         df.replace(to_replace=[None,"None"], value='NA', inplace=True) # None value replace by 'NA' Text
#         df.replace(to_replace=[0,"0"], value='', inplace=True) # None value replace by '' Text
#         df.replace(to_replace=["False"], value='no', inplace=True) # False value replace by 'no' Text
#         df.replace(to_replace=["True"], value='yes', inplace=True) # True value replace by 'yes' Text

#         if sl:
#             df.index = np.arange(1, len(df) + 1) # starting index from 1

#         if extension_type == 'xlsx':
#             if sl:
#                 if headers:
#                     df.to_excel(writer, sheet_name='Sheet1', startrow=1,index=True, header=headers,index_label = index_label)
#                 else:
#                     df.to_excel(writer, sheet_name='Sheet1', startrow=1,index=True, index_label = index_label)
#             else:
#                 if headers:
#                     df.to_excel(writer, sheet_name='Sheet1', startrow=1, index=None, header=headers)
#                 else:
#                     df.to_excel(writer, sheet_name='Sheet1', startrow=1, index=None)
#         #print(df)
                
#         # Get the dimensions of the dataframe.
#         (max_row, max_col) = df.shape
#         workbook  = writer.book
#         worksheet = writer.sheets['Sheet1']
        
#         if extra_data_on_top:
#             merge_format = {
#                             'bold': 1,
#                             'border': 1,
#                             'align': 'center',
#                             'valign': 'vcenter',
#                             'fg_color': '#f4bb0e',
#                             'font_size':13
#                             }
#             merge_format = workbook.add_format(merge_format)
#             for i, each in enumerate(extra_data_on_top):
#                 worksheet.merge_range('B'+str(i+1)+':C'+str(i+1),each,merge_format)
            
#         header_fmt = workbook.add_format({'bg_color':'green','font_color':'white','align':'center','border':1,'border_color':'white'})
#         header_sl_fmt = workbook.add_format({'bg_color':'#3366FF','font_color':'white','align':'center'})
        
#         text_wrap_format = workbook.add_format({'text_wrap': True,'align':'center','valign': 'vcenter',})
        
#         # if sl:
#         #     worksheet.set_column(1,max_col,20,text_wrap_format) # For cell width set and text wrap set
#         # else:
#         #     worksheet.set_column(0,max_col,12,text_wrap_format) # For cell width set and text wrap set
        
#         if headers:
#             for col_num, value in enumerate(headers):
#                 if len(value) >= 4:
#                     cell_value = 13
#                 else:
#                     cell_value = 6
#                 if sl:
#                     worksheet.write(1, col_num + 1 , value, header_fmt) # For header cell formatting
#                 else:
#                     worksheet.write(1, col_num , value, header_fmt) # For header cell formatting
                
#                 worksheet.set_column(col_num,max_col,cell_value,text_wrap_format) # For cell width set and text wrap set

#         else:
#             for col_num, value in enumerate(df.columns.values):
#                 if len(value) >= 4:
#                     cell_value = 14
#                 else:
#                     cell_value = 7
                    
#                 if sl:
#                     worksheet.write(1, col_num + 1, value, header_fmt)
#                 else:
#                     worksheet.write(1, col_num , value, header_fmt)

#                 worksheet.set_column(col_num,max_col,cell_value,text_wrap_format) # For cell width set and text wrap set
            
#         if sl:
#             worksheet.write('A2', index_label, header_sl_fmt) # For sl_no cell formatting

#         # format_object1 = workbook.add_format({'num_format': '# 0.00'})
#         # worksheet.set_column('H:H', 20, format_object1)


#         if extra_header:
#             merge_format = workbook.add_format(extra_header['merge_format'])
#             for each in extra_header['merge_range']:
#                 worksheet.merge_range(each['range'], each['text'], merge_format)
#             if 'no_hight' in extra_header and not extra_header['no_hight']:
#                 worksheet.set_row(0, 25) # Row Hight

#         if column_bg:
#             for each in column_bg:
#                 bg_fmt = workbook.add_format({'bg_color':each['bg_color'],'align':'center','border':1,'border_color':'white'})
#                 worksheet.write(each['name'], each['text'], bg_fmt) # For sl_no cell formatting
#     if autofilter:
#         worksheet.autofilter(1, 0, max_row, max_col-int(autofilter['upto'])) # For autofilter set
        
#     writer.save()
#     url = getHostWithPort(request) + file_path_name if file_path_name else None
#     return url

# def get_full_name_of_user(user_id):
#     from django.db.models.functions import Concat
#     from django.db.models import F, Value, CharField

#     if type(user_id) == list:
#         return User.objects.filter(
#             pk__in=user_id).annotate(
#                 name=Concat(F('first_name'), Value(' '), F('last_name'), output_field=CharField())).values_list('name',flat=True)
#     else:
#         return User.objects.get(pk=user_id).get_full_name()

# def get_previous_week_date_by_date(date):
#     date = str(date)[0:10]
#     date = datetime.strptime(date,'%Y-%m-%d')
#     start_date = date + timedelta(-date.weekday(), weeks=-1)
#     end_date = date + timedelta(-date.weekday() - 2)
#     return start_date,end_date

# def get_abbreviation(s):
#       splitted_string=s.split()
#       string=""
#       for word in splitted_string:
#          if word != "and":
#             string += str(word[0])
#       return string.upper()
