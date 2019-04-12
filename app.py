from myprojecct import app, db 
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user,login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm