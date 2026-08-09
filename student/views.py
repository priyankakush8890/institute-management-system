from django.shortcuts import render, redirect, HttpResponse
from stuapp.emailbackend import emailbackend
from django.contrib.auth import authenticate, logout, login
from stuapp.models import CustomUser, Student, FeePayment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import razorpay

client = razorpay.Client(
    auth=(
        settings.RAZORPAY_KEY_ID,
        settings.RAZORPAY_KEY_SECRET
    )
)

@login_required(login_url='/')
def fee_payment(request):

    student = Student.objects.get(
        admin=request.user
    )

    payments = FeePayment.objects.filter(
        student=student
    ).order_by('-created_at')

    total_fee = 50000
    paid_amount = sum(
        float(payment.amount)
        for payment in payments
        if payment.status == 'Success'
    )

    pending_amount = total_fee - paid_amount

    return render(
        request,
        'student/student_feepayment.html',
        {
            'student': student,
            'payments': payments,
            'total_fee': total_fee,
            'paid_amount': paid_amount,
            'pending_amount': pending_amount,
        }
    )

@login_required(login_url='/')
def payment_history(request):

    student = Student.objects.get(
        admin=request.user
    )

    payments = FeePayment.objects.filter(
        student=student
    ).order_by('-created_at')

    return render(
        request,
        'student/payment_history.html',
        {
            'student': student,
            'payments': payments
        }
    )
@login_required(login_url='/')
def create_payment(request):

    student = Student.objects.get(
        admin=request.user
    )

    payments = FeePayment.objects.filter(
        student=student
    ).order_by('-created_at')

    total_fee = 50000

    paid_amount = sum(
        float(payment.amount)
        for payment in payments
        if payment.status == 'Success'
    )

    pending_amount = total_fee - paid_amount

    if pending_amount <= 0:
        messages.info(
            request,
            'Your fees are already fully paid.'
        )
        return redirect('fee_payment')

    # Razorpay expects amount in paise
    amount = int(pending_amount * 100)

    order = client.order.create({
        'amount': amount,
        'currency': 'INR',
        'receipt': f'fee_{student.id}',
        'payment_capture': 1
    })

    FeePayment.objects.create(
        student=student,
        amount=pending_amount,
        razorpay_order_id=order['id'],
        status='Pending'
    )

    return render(
        request,
        'student/student_feepayment.html',
        {
            'student': student,
            'order': order,
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'payments': payments,
            'total_fee': total_fee,
            'paid_amount': paid_amount,
            'pending_amount': pending_amount,
        }
    )
@login_required(login_url='/')
def payment_success(request):

    if request.method != 'POST':
        return redirect('fee_payment')

    payment_id = request.POST.get('razorpay_payment_id')
    order_id = request.POST.get('razorpay_order_id')
    signature = request.POST.get('razorpay_signature')

    try:
        payment = FeePayment.objects.get(
            razorpay_order_id=order_id,
            student__admin=request.user
        )

        # Verify Razorpay signature
        client.utility.verify_payment_signature({
            'razorpay_order_id': payment.razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        })

        # Signature verified successfully
        payment.razorpay_payment_id = payment_id
        payment.razorpay_signature = signature
        payment.status = 'Success'
        payment.save()

        messages.success(
            request,
            'Payment completed successfully!'
        )

        return redirect('fee_payment')

    except razorpay.errors.SignatureVerificationError:
        messages.error(
            request,
            'Payment verification failed.'
        )

        return redirect('fee_payment')

    except FeePayment.DoesNotExist:
        messages.error(
            request,
            'Payment order not found.'
        )

        return redirect('fee_payment')

    
def base(request):
    return render(request,'base.html') 


def loginn(request):
    return render(request,'login.html')

def dologin(request):
    
    if request.method == "POST":
       user = emailbackend.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       if user!=None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect('hodhome')
            # return HttpResponse('This is hod Panel')
           elif user_type == '2':
               return redirect('staffhome')
           elif user_type == '3':
               return redirect('studenthome')
           else:
               messages.error(request,'Email and Password Are Invalid !')
               return redirect('loginn')
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('loginn')
       
       
def dologout(request):
    logout(request)
    return redirect('loginn')


@login_required(login_url='/')
def profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    dict={
        'user':user,
    }
    
    return render(request,'profile.html')

@login_required(login_url='/')
  
def profileUpdate(request):
    if request.method=='POST':
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get ('password')
        
        
        try:
            user=CustomUser.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            
            if password!=None and password!="":
                user.set_password(password)
            if profile_pic !=None and profile_pic != "":
                user.profile_pic = profile_pic
            user.save()   
            messages.success(request,"Updated successfully")
            return redirect('profile')
        except:
            messages.error(request,'error occured')
            
            
    return render(request,'profile.html')