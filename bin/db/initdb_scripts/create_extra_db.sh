#!/usr/bin/env sh
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_id
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_baggins
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_pre_matricula
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_seletivo
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_selecao
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_integrador_ms
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_integrador_ui
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_dashboard
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_avaportal
