<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{profile_content["admin_specific_content"]["profile_admin_hour_registration"]["decorative_header_text"]}}
    </p>
    <h2>
      <!-- prettier-ignore -->
      {{profile_content["admin_specific_content"]["profile_admin_hour_registration"]["header_text"]}}
    </h2>
  </div>
  <div>
    <div id="content_box_styling">
      <div id="content_box_header_styling">
        <div
          class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
        >
          <div id="icon_medium" class="text-unidDarkBlue">
            % include(global_content['ui_icons']['stop_watch'])
          </div>
          <p class="font-bold text-lg text-unidDarkBlue">Timeregistrering</p>
        </div>
      </div>
      <div class="flex flex-col gap-10 p-6 text-unidPurple">
        <form id="taskForm" class="space-y-8 w-full">
          <div class="flex flex-col gap-2 text-sm">
            <div class="space-y-1">
              <p id="form_label">Brugeroplysninger</p>
              <hr />
            </div>
            <div class="">
              <div class="grid grid-cols-6 gap-2 items-center">
                <label for="customer" class="grid col-span-2">
                  <p class="font-semibold text-unidDarkBlue">Vælg kunde:</p>
                </label>
                <select
                  id="customer"
                  name="customer"
                  class="w-full py-2 px-5 grid col-span-4 rounded-md border border-unidLightBlue placeholder:text-unidLightBlue text-unidDarkBlue transition ease-in-out duration-300 focus:ring-2 focus:ring-unidYellow focus:outline-none"
                  placeholder="Choose a customer…"
                >
                  % for customer in active_customers:
                  <option
                    required
                    id="form_input"
                    value="{{ customer['user_id'] }}"
                  >
                    {{ customer["first_name"] }} {{ customer["last_name"] }}
                  </option>
                  % end
                </select>
              </div>
            </div>
          </div>
          <div class="flex flex-col gap-2 text-sm">
            <div class="space-y-1">
              <p id="form_label">Opgaveoplysninger</p>
              <hr />
            </div>
            <div class="grid lg:grid-cols-6 gap-2 items-center">
              <label for="title" class="grid lg:col-span-2">
                <p class="font-semibold text-unidDarkBlue">Opgavetitel:</p>
              </label>
              <textarea
                class="w-full py-2 px-5 grid lg:col-span-4 rounded-md border border-unidLightBlue placeholder:italic placeholder:text-unidLightBlue text-unidDarkBlue transition ease-in-out duration-300"
                id="title"
                name="title"
                accept-charset="UTF-8"
                placeholder="Titel på udførte opgave"
                required
              ></textarea>
            </div>
            <div class="grid lg:grid-cols-6 gap-2 items-center">
              <label for="description" class="grid lg:col-span-2">
                <p class="font-semibold text-unidDarkBlue">
                  Opgavebeskrivelse:
                </p>
              </label>
              <textarea
                class="w-full py-2 px-5 grid lg:col-span-4 rounded-md border border-unidLightBlue placeholder:italic placeholder:text-unidLightBlue text-unidDarkBlue transition ease-in-out duration-300"
                id="description"
                name="description"
                accept-charset="UTF-8"
                placeholder="Beskrivelse af udførte opgave..."
                required
              ></textarea>
            </div>
          </div>
          <div class="flex flex-col gap-2 text-sm">
            <div class="space-y-1">
              <p id="form_label">Tid</p>
              <hr />
            </div>
            <div class="grid md:grid-cols-6 space-y-2 items-center">
              <label for="hours" class="grid col-span-2">
                <p class="font-semibold text-unidDarkBlue">Tid brugt:</p>
              </label>
              <div class="grid col-span-4">
                <div class="flex justify-between w-fit md:justify-normal gap-4">
                  <div class="flex items-center gap-2">
                    <input
                      class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:text-unidLightBlue text-unidDarkBlue transition ease-in-out duration-300"
                      type="number"
                      id="hours"
                      name="hours"
                      min="0"
                      step="1"
                      placeholder="0"
                    />
                    <p>timer</p>
                  </div>
                  <div class="flex items-center gap-2">
                    <input
                      class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:text-unidLightBlue text-unidDarkBlue transition ease-in-out duration-300"
                      type="number"
                      id="minutes"
                      name="minutes"
                      min="0"
                      max="59"
                      step="1"
                      placeholder="0"
                    />
                    <p>minutter</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="space-y-4 w-fit mx-auto">
            <div id="submitTaskButton">
              <button type="button" id="primary_button">Registrer</button>
            </div>
            <p
              id="taskSubmissionMessage"
              style="display: none"
              class="text-unidLightBlue text-sm"
            ></p>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
