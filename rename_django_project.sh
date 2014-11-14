#!/usr/bin/env bash

echo "New django name?"
read new_django_name

project_path=$(pwd)
old_django_name=$(python -c "import os;print os.path.split('$project_path')[1]")
old_django_path_profix=$(python -c "import os;print os.path.split('$project_path')[0]")
new_project_path=$(python -c "import os; print os.path.join('$old_django_path_profix', '$new_django_name')")
cp -r $project_path $new_project_path
django_base=$(python -c "import os; print os.path.join('$new_project_path', '$old_django_name')")
if [ -d $django_base ];
then
  new_django_base=$(python -c "import os; print os.path.join('$new_project_path', '$new_django_name')")
  mv $django_base $new_django_base
fi
cd $new_project_path && $(grep $old_django_name -ril ./ | xargs sed -i "s/$old_django_name/$new_django_name/g")
echo "new files in: $new_project_path"
echo "please 'cd $new_project_path && grep $old_django_name -ril' all if all string has replaced!"
echo "done"
